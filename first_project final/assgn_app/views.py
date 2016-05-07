from django.shortcuts import render,render_to_response

from django.http import HttpResponse,HttpResponseRedirect

from django.contrib import auth

from django.core.context_processors import csrf 

from .models import Student,Professor,AssignmentQ,AssignmentA,Subject,StudSub

from .forms import UploadFileForm,AssgnQFileForm

from datetime import date

user_id = 0

def index(request):
	return render_to_response('welcome.html')
	
def stud_login(request):
	c={}
	c.update(csrf(request))
	return render_to_response('login.html',c)
	
def auth_view(request):
	if request.method == 'POST':
		stud_id = request.POST.get('stud_id','')
		password = request.POST.get('password','')
		request.session['stud_id'] = stud_id
		request.session['stud_password'] = password 
		user = Student.objects.filter(unique_id=stud_id, password=password)
		if len(user)==0:
			c = {'msg':'ID or password incorrect'}
			c.update((csrf(request)))
			return render_to_response('login.html',c)
		user = Student.objects.filter(unique_id=stud_id, password=password).first()
		assgnAnsList = AssignmentA.objects.filter(unique_id=user)
		par = {'uname':Student.objects.filter(unique_id=stud_id).first(), 
		'subjList':StudSub.objects.filter(stud_id=stud_id),'uid':stud_id,'assgnAnsList':assgnAnsList}
		par.update(csrf(request))
		c={}
		c.update((csrf(request)))
		return render_to_response('logged_in.html',par)
		
	else:
		if request.session.get('stud_id', ''):
			user = Student.objects.filter(unique_id=request.session['stud_id'], password=request.session['stud_password']).first()
			stud_id = request.session['stud_id']
			assgnAnsList = AssignmentA.objects.filter(unique_id=Student.objects.get(unique_id=stud_id))
			par = {'uname':Student.objects.filter(unique_id=request.session['stud_id']).first(), 
			'subjList':StudSub.objects.filter(stud_id=stud_id),'uid':stud_id,'assgnAnsList':assgnAnsList}
			par.update(csrf(request))
			c={}
			c.update((csrf(request)))
			if user is not None:
				return render_to_response('logged_in.html',par)
			else:
				return render_to_response('login.html',c)				
		else:
			c = {'msg':'you must login first'}
			return render_to_response('welcome.html',c)
def register(request):
	if request.method=='POST':
		fname = request.POST.get('fname','')
		lname = request.POST.get('lname','')
		unique_id = request.POST.get('uid','')
		password = request.POST.get('pass','')
		global user_id
		user_id = int(unique_id)
		print(user_id)
		obj = Student(unique_id=unique_id,fname=fname,lname=lname,password = password)
		obj.save()
		
		c={'uid':user_id,'subjList':Subject.objects.all()}
		c.update(csrf(request))
		return render_to_response('registered.html',c)
	elif request.method == 'GET':	
		c={}
		c.update(csrf(request))
		return render_to_response('register.html',c)

def reg_subj(request):
	if request.method=='POST':
		c={'subjList':Subject.objects.all()}
		c.update(csrf(request))
		checklist = request.POST.getlist('check[]')
		#fetch from subjects table and display in register.html. 
		for subj in checklist:
			global user_id
			print(user_id)
			stud = Student.objects.get(unique_id=(user_id))
			sub = Subject.objects.get(subj_id = subj)
			obj = StudSub(stud_id = stud,subj_id = sub)
			obj.save()
		return render_to_response('login.html',c)

def logged_in(request):
	c={}
	c.update(csrf(request))
	return render_to_response('logged_in.html',c)

def prof_login(request):
	c={}
	c.update(csrf(request))
	return render_to_response('prof_login.html',c)
	
def prof_auth_view(request):
	if request.method=='POST':
		prof_id = request.POST.get('prof_id','')
		password = request.POST.get('password','')
		request.session['prof_id'] = prof_id
		request.session['password'] = password
		user = Professor.objects.filter(prof_id=prof_id, password=password)
		if len(user)==0:
			c = {'msg':'ID or password incorrect'}
			c.update((csrf(request)))
			return render_to_response('prof_login.html',c)
		subjList = Subject.objects.filter(prof_id=prof_id)	
		par = {
			'uname':Professor.objects.filter(prof_id=prof_id).first(),
			'subjList':subjList
		}
	
		par.update(csrf(request))
		c={}
		c.update((csrf(request)))
		if user is not None:
			return render_to_response('prof_loggedin.html',par)
		else:
			return render_to_response('prof_login.html',c)
	else:
		prof_id = request.session.get('prof_id','')
		password = request.session.get('password','')
		
		user = Professor.objects.filter(prof_id=prof_id, password=password).first()
		subjList = Subject.objects.filter(prof_id=prof_id)	
		par = {
			'uname':Professor.objects.filter(prof_id=prof_id).first(),
			'subjList':subjList
		}
	
		par.update(csrf(request))
		c={}
		c.update((csrf(request)))
		if user is not None:
			return render_to_response('prof_loggedin.html',par)
		else:
			return render_to_response('prof_login.html',c)

def assgn_page(request):
	if request.method == 'POST':
		stud_id = request.session['stud_id']
		subj_id = request.POST.get('subject','')
		assgnList = AssignmentQ.objects.filter(subj_id=subj_id, due_date__gte = date.today())
		assgnListExp = AssignmentQ.objects.filter(subj_id=subj_id, due_date__lt = date.today())
		form = UploadFileForm()
		return render(request,'assgn_page.html',{'form':form,'uid':stud_id,'assgnList':assgnList,'assgnListExp':assgnListExp,
		'subj':subj_id})


def upload_assgn(request):
	if request.method == 'POST':
		uid = request.session['stud_id']
		stud = Student.objects.get(unique_id=uid)
		assg = AssignmentQ.objects.get(assgn_id=request.POST.get('assgn_id',''))
		fil = request.FILES['docfile']
		#obj = AssignmentA(assgn_a_file = fil,assgn_id=assg,unique_id=stud)
		#obj.save()
		obj = AssignmentA.objects.filter(assgn_id=assg,unique_id=stud)
		if obj:			#guaranteed to be a singleton as unique_together enforced
			obj = AssignmentA.objects.get(assgn_id=assg,unique_id=stud)
			obj.assgn_a_file = fil
			obj.save()
		else:
			obj = AssignmentA(assgn_a_file = fil,assgn_id=assg,unique_id=stud)	
			obj.save()	
		c={}
		c.update(csrf(request))
		return render_to_response('upload_success.html',c)
		
def selected_subj(request):
	if request.method == 'POST':
		subj_id = request.POST.get('subject','')
		request.session['subj_id'] = subj_id
		assgnList = AssignmentQ.objects.filter(subj_id=subj_id)
		form = AssgnQFileForm()
		c = {'assgnList':assgnList, 'form':form, 'subj_id':subj_id}
		c.update(csrf(request))
		return render(request,'prof_uplink.html',c)
		
def stud_submitted(request):
	if request.method == 'POST':
		assgn_id = request.POST.get('assgn','')
		assgnList = AssignmentA.objects.filter(assgn_id=assgn_id)
		#studList = Student.objects.all() 
		c = {'assgnList':assgnList}
		c.update(csrf(request))
		return render(request,'uploaded_studs.html',c)
	
def upload_success(request):
	if request.method == 'POST':
		assgn_id = request.POST.get('assgn_id','')
		subj_id = request.session['subj_id']
		subj = Subject.objects.get(subj_id = subj_id)
		fil = request.FILES['docfile']
		date = request.POST.get('due_on','')
		obj = AssignmentQ(assgn_id=assgn_id, subj_id = subj, assgn_q_file = fil,due_date = date)
		obj.save()
		return render_to_response('upload_success_prof.html')
		
def save_marks(request):
	if request.method == 'POST':
		stud = Student.objects.get(unique_id=int(request.POST.get('uid','0')))
		assgnQ = AssignmentQ.objects.get(assgn_id=request.POST.get('assgn_id',''))
		obj = AssignmentA.objects.get(assgn_id = assgnQ, unique_id=stud)
		obj.marks = int(request.POST.get('marks','-1'))
		obj.save()
		assgnList = AssignmentA.objects.filter(assgn_id=request.POST.get('assgn_id',''))
		#studList = Student.objects.all() 
		c = {'assgnList':assgnList}
		c.update(csrf(request))
		return render(request,'uploaded_studs.html',c)
		
def logout(request):
	msg = 'You are logged out'
	if request.session.get('stud_id',''):
		del request.session['stud_id']
		del request.session['stud_password']
	elif request.session.get('subj_id',''):
		del request.session['subj_id']
		del request.session['prof_id']
		del request.session['password']
	else:
		msg = 'Already logged out.'
	return render(request,'welcome.html',{'msg':msg,})
