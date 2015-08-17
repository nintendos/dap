#-*-coding:utf-8-*-
import sys
import os
import chardet
import json
# from django.utils import simplejson
from datetime import date,datetime
import pytz
from django.template import RequestContext
from django.template.loader import get_template
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from models import Project,Task
from engine.forms.form import CreateTaskForm
from django.shortcuts import render_to_response
# import upyun
import uuid
import re
from bs4 import BeautifulSoup
import mptt

class CJsonEncoder(json.JSONEncoder): #解决Python自带的json序列化工具不能序列化datetime类型数据问题
	def default(self, obj):
		if isinstance(obj, datetime):
			tz = pytz.timezone('Asia/Shanghai')
			return obj.now(tz).strftime('%Y年%m月%d日 %H:%M')
		elif isinstance(obj, date):
			return obj.strftime('%Y年%m月%d日')
		else:
			return json.JSONEncoder.default(self, obj)

def home(request):
	task_list = Task.objects.all().order_by("tid").reverse()
	project_list = Project.objects.all()
	return render_to_response('home.html',{
		'task_list':task_list,
		'project_list':project_list,		
		},context_instance =RequestContext(request))



def task(request, link):
	task = Task.objects.get(tid=link)
	brand_id = task.brand_id
	brand = Brand.objects.get(bid=brand_id)
	project = task.project
	project_list = project.get_ancestors(ascending=False, include_self=True)
	return render_to_response('task.html',{
		'name':task.name,
		'tid':task.tid,
		'project':project_list,
		'brand':brand,
		'description':task.description,
		},context_instance =RequestContext(request))

@login_required
def create_task(request):
	all_brand = Brand.objects.all().reverse()
	all_project = Term.objects.filter(taxonomy="C").reverse()
	brand_list = list(all_brand.order_by("bid"))
	project_list = list(all_project.order_by("term_id"))	
	return render_to_response('edit-task.html',{
		'brand_list':brand_list,
		'project_list':project_list
		},
		context_instance =RequestContext(request))

@login_required
def edit_task(request): #用于加载编辑页面
	tid = request.GET["tid"]
	task = Task.objects.get(tid=tid)
	all_brand = Brand.objects.all().reverse()
	all_project = Term.objects.filter(taxonomy="C").reverse()
	brand_list = list(all_brand.order_by("bid"))
	project_list = list(all_project.order_by("term_id"))
	pic_list = list(Pic.objects.filter(task=tid))
	return render_to_response('edit-task.html',{
		"tid":task.tid,
		"task_name":task.name,
		"task_description":task.description,
		"brand":task.brand,
		'brand_list':brand_list,
		"project":task.project,
		'project_list':project_list,
		"pic_list":pic_list,
		"thumbnail":task.thumbnail,
		},context_instance =RequestContext(request))


@login_required
def save_task(request):
	if request.method == "POST":
		t = get_template('edit-task.html') 
		f = CreateTaskForm(data = request.POST)
		tid = request.POST['tid'] 
		name = request.POST['name']
		description = request.POST['description']
		brand = request.POST['brand'] 
		project = request.POST['project'] 
		soup = BeautifulSoup(description)			
		if not request.POST.has_key("thumbnail"):#没有上传缩略图的新产品
			thumbnail = "" #可改为-1
		else:
			thumbnail = request.POST["thumbnail"]
		img = soup.findAll(src=re.compile("^http://img.dapizi.com/"))
		# tag = request.POST['tag'] 

		if not request.POST.has_key("project"):
			return HttpResponse("未选择分类")#不起作用?

		# if request.POST["tag"]:
		# 	tag = ','.join(request.POST.getlist("tag"))          

		if f.is_valid():
			h = Task(name=name,description=description,brand_id=brand,project_id=project,thumbnail_id=thumbnail)
			try: #判断Task是否已存在
				Task.objects.get(tid=tid)
			except ObjectDoesNotExist: #不存在则入库
				h.save()
			except: #tid为空或其他异常时
				h.save()
			else:
				f.update() #新建产品时，使用已存在的名称，并上传一张图片选中会报错
			finally:
				if tid=="":
					task = Task.objects.get(name=name)
				else:
					task = Task.objects.get(tid=tid)
				for i in img:
					s = i["src"]
					try:
						Pic.objects.get(url=s)
					except ObjectDoesNotExist:
						return HttpResponse("图片不存在")
					else:
						pic = Pic.objects.get(url=s)
						pic.task_id=task.tid
						pic.category="H"
						pic.save()
				#保存缩略图
				try:
					Pic.objects.get(pic_id=thumbnail)
				except ObjectDoesNotExist:
					return HttpResponse("<p>记得上传缩略图</p><a href='/'>回到首页</a>")#需要吗?
				except:
					return HttpResponse("<p>Thumbnail为空，记得上传</p><a href='/'>回到首页</a>")#新添加产品未传图片,Thumbnail id为Null
				else:
					pic = Pic.objects.get(pic_id=thumbnail)
					pic.task_id=task.tid
					pic.category="H"
					pic.save()

				# for i in tag.split(','): #保存标签
				# 	term = Term.objects.get(term_id=i)
				# 	u.terms.add(term)
			# payload = {
			# 	'tid':u.tid,
			# 	'msg': "商品已保存",
			# 	'success': True}

			return HttpResponseRedirect('/edit-task/?tid='+str(task.tid))

		else:
			content_html = t.render(RequestContext(request,{
				'f':f,
				}))
			payload = {
				'content_html': content_html,
				'success': False}
			return HttpResponse(json.dumps(payload),mimetype="application/json")

	return HttpResponseRedirect('/')


@login_required
def del_task(request):
	request.session['ref'] = request.META.get('HTTP_REFERER', '/')  ##记住来源url，如没有则为首页('/')
	tid = request.GET.get("tid")
	task = Task(tid=tid)
	return HttpResponseRedirect(request.session['ref']) 


