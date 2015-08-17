#-*-coding:utf-8-*-
from django import forms
from engine.forms.field import CreateTaskField
from django.forms.fields import CharField
from engine.models import Project,Task

class CreateTaskForm(forms.Form):
	name = CreateTaskField(required=True)
	tid = CreateTaskField(required=False)
	description = CreateTaskField(required=True)
	priority = CreateTaskField(required=True)

	def get_id(self):
		return self.cleaned_data['tid']

	def update(self):
		task = Task.objects.get(tid = self.get_id()) 
		task.name = self.cleaned_data['name']
		task.description = self.cleaned_data['description']
		task.priority = self.cleaned_data['priority']
		task.thumbnail_id = self.cleaned_data['thumbnail']
		task.save()
