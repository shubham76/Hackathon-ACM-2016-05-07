from django import forms
from django.db import models
import datetime

class UploadFileForm(forms.Form):
	docfile = forms.FileField()
	
class AssgnQFileForm(forms.Form):
	assgn_id = forms.CharField(max_length=20)
	docfile = forms.FileField()
	#due_on = forms.DateField(initial = datetime.date.today)
