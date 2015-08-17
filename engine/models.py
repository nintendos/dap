#-*-coding:utf-8-*-

from django.db import models
from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from userena.models import UserenaBaseProfile
# from tinymce.models import HTMLField

# class Actor(models.Model):
# 	bid = models.AutoField(u'编号', max_length=255, primary_key=True)
# 	name = models.CharField(u'姓名', max_length=255, blank=False, null=False, unique=True)
# 	email = models.EmailField(u'Email', blank=True, null=True)
# 	# logo = models.ForeignKey('Pic', null=True, blank=True, on_delete=models.SET_NULL, limit_choices_to={'category': "B"})
# 	role_name = models.ForeignKey('Role', verbose_name="角色")

# 	def __unicode__(self):
# 		return self.name

# class Role(models.Model):
# 	name = models.CharField(u'角色名称', max_length=255, blank=False, null=False)
# 	department = models.CharField(u'所属部门', max_length=255, blank=False, null=False)

# 	def __unicode__(self):
# 		return self.name
		

#Status 	int 	0 	状态：0禁用，1启用
#Priority 	int 	0 	优先级，越大，同级显示的时候越靠前
class Project(MPTTModel):
	p_id = models.AutoField(u'项目编号', max_length=255, primary_key=True)
	p_name = models.CharField(u'项目名称', max_length=255, unique=True)
	summary = models.CharField(u'项目简介', max_length=255, null=True, blank=True)
	description = models.TextField(u'项目描述')
	parent = TreeForeignKey('self', related_name='children',null=True, blank=True, default = None)
	# thumbnail = models.ForeignKey('Pic', null=True, blank=True, verbose_name="项目缩略图", related_name="term_thumbnail",limit_choices_to={"category":"C"})
	# actor = models.ForeignKey('Actor', verbose_name="参与者", related_name = 'member') 
	# actor = models.ManyToManyField('Actor', related_name="actor_set")
	# project_leader = models.ForeignKey('Actor', verbose_name="项目经理", related_name = 'pm') 
	active_status = models.BooleanField(default=1)
	
	def __unicode__(self):
		return self.p_name

	# It is required to rebuild tree after save, when using order for mptt-tree
	def save(self, *args, **kwargs):
		super(Project, self).save(*args, **kwargs)
		Project.objects.rebuild()

    # Sortable property
	order = models.PositiveIntegerField()

	class MPTTMeta:
		order_insertion_by=['order']


class Task(models.Model):
	tid = models.AutoField(u'任务编号', max_length=255, primary_key=True)
	name = models.CharField(u'任务名称', blank=False, max_length=255)
	project = models.ForeignKey('Project',  verbose_name="所属项目") 
	description = models.TextField()	
	# cat = models.ForeignKey('Project',  verbose_name="所属产品") 
	# tags = models.ManyToManyField('Project', related_name="tag_set")
	priority = models.CharField(u'优先级', max_length=255)
    # score = models.PositiveIntegerField(default=0)
    # upvotes = models.PositiveIntegerField(default=0)
    # downvotes = models.PositiveIntegerField(default=0)

	def __unicode__(self):
		return self.name


class MyProfile(UserenaBaseProfile):
	user = models.OneToOneField(User, unique=True, verbose_name=_('user'), related_name='my_profile')
	favourite_snack = models.CharField(_('favourite snack'), max_length=5)
