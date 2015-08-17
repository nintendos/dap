#-*-coding:utf-8-*-
import sys
import os
import json
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from models import Project
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
import upyun
import uuid
import mptt
from django.views.decorators.csrf import csrf_exempt
# from engine.unordered_list import unordered_list


# def display(terms):
# 	display_list = []
# 	for term in terms:
# 		display_list.append(term.term_name)
# 		children = term.children.all()
# 		if len(children) > 0:
# 			display_list.append(display(term.children.all()))
	
# 	return display_list

def project_list(request):
	roots = Term.objects.filter(parent=None,taxonomy="C")
	return render_to_response('project_list.html', {
		# 'var': unordered_list(var)
		'roots': roots
		},context_instance =RequestContext(request))



def project(request, link):
	project = Term.objects.get(term_id=link)
	children = project.children.all()
	return render_to_response('project.html',{
		'project':project,
		# 'name':project.term_name,
		# 'description':project.description,
		'children':children,
		},context_instance =RequestContext(request))


# @csrf_exempt
# def project_thumbnail_upload(request):
# 	if request.is_ajax():
# 		_request  = request
# 		uploaded  = _request.read
# 		file_size = int(uploaded.im_self.META["CONTENT_LENGTH"])
# 		file_name = request.GET.get('qqfile')
# 		# term_id = request.GET.get('term_id')
# 		name, ext = os.path.splitext(file_name)
# 		file_name = str(uuid.uuid1())
# 		file_name = file_name+ext.encode("utf-8")
# 		file_dir = "project"
# 		_u = upyun.UpYun('dapizi','dapizi','leap2006',timeout=30, endpoint=upyun.ED_AUTO)
# 		_u.put('/%s/%s' % (file_dir, file_name),_request.read(file_size), True) 
# 		img_url = "http://img.dapizi.com/%s/%s" % (file_dir, file_name)#可使用如request.user.id
# 		pic = Pic(url=img_url,pic_title=file_name,category="C")#,huo_id=hid,category="H"
# 		pic.save()

# 		payload = {
# 			'pic_id': pic.pic_id,
# 			'img_url': img_url,
# 			'success': True}
# 		return HttpResponse(json.dumps(payload),mimetype="application/json")

# 	return HttpResponseRedirect('/')
