#-*-coding:utf-8-*-

import re
from django.forms.fields import Field,CharField
from django.core.exceptions import ValidationError


class CreateTaskField(CharField):
	default_error_messages = {
		'required':u'请输入正确的任务名称。',
	}
	
	def clean(self,value):
		value = self.to_python(value).strip()
		return super(CreateTaskField, self).clean(value)

