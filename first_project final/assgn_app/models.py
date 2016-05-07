from django.db import models
from time import time
from datetime import date
# Create your models here.

class Student(models.Model):
	unique_id = models.IntegerField(null=False,primary_key=True)
	fname = models.CharField(max_length=20)
	lname = models.CharField(max_length=20)
	password = models.CharField(max_length=20)
	def __str__(self):
		return str(self.unique_id) + ' / ' + self.fname

class Professor(models.Model):
	prof_id = models.IntegerField(null=False,primary_key=True)
	fname = models.CharField(max_length=20)
	lname = models.CharField(max_length=20)
	password = models.CharField(max_length=20)
	def __str__(self):
		return str(self.prof_id) + ' / ' + self.fname
		
		
class Subject(models.Model):
	subj_id = models.CharField(max_length=20, primary_key=True)
	subj_name = models.CharField(max_length=30)
	prof_id = models.ForeignKey(Professor)
	semester = models.IntegerField()
	def __str__(self):
		return self.subj_id
	
class StudSub(models.Model):
	stud_id = models.ForeignKey(Student)
	subj_id = models.ForeignKey(Subject)
	def __str__(self):
		return str(self.stud_id.unique_id) + '/' + self.subj_id.subj_id




class AssignmentQ(models.Model):
	class Meta:
		unique_together = (('assgn_id','subj_id'),)
	assgn_id = models.CharField(max_length=10,primary_key=True)
	subj_id = models.ForeignKey(Subject)
	assgn_q_file = models.FileField(upload_to = "assgn_ques")
	due_date = models.DateField(default=date.today)
	def __str__(self):
		return str(self.assgn_id + self.subj_id.subj_id)
	
	
class AssignmentA(models.Model):
	class Meta:
		unique_together = (('unique_id','assgn_id'),)
	unique_id = models.ForeignKey(Student)
	assgn_id = models.ForeignKey(AssignmentQ)
	assgn_a_file =  models.FileField(upload_to = "assgn_ans")
	marks = models.IntegerField(default=-1)
	sub_date = models.DateField(default=date.today)
	def __str__(self):
		return str(self.assgn_id.assgn_id + ' / ' + str(self.unique_id.unique_id))
