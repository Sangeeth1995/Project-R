from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponse
from Students.forms import UserAddForm,StudentAddForm,LoginForm
from Students.models import Students,Projects
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login


@login_required
@csrf_exempt
def project_add_view(request):
	d={}
	form=StudentAddForm()
	
	if request.method=='POST':
		form=StudentAddForm(request.POST)
		if form.is_valid():
			# student=Projects()
			# student.Projectname = form.cleaned_data['Projectname']
			# student.Projectyear = form.cleaned_data['Projectyear']
			# student.Branch = form.cleaned_data['Branch']
			# student.Projectdescription = form.cleaned_data['Projectdescription']
			# d['students']=	Projects.objects.all()
			Projectname = form.cleaned_data['Projectname']
			Projectyear = form.cleaned_data['Projectyear']
			Branch = form.cleaned_data['Branch']
			Projectdescription = form.cleaned_data['Projectdescription']
			demo=Projects(Projectname=Projectname,Projectyear=Projectyear,Branch=Branch,Projectdescription=Projectdescription)
			demo.save()
			return redirect('project_add')
	d['form']=form
	return render(request,'project_add.html',d)
@csrf_exempt
def user_register(request):
	d={}
	user=UserAddForm()
	if request.method=='POST':
		form=UserAddForm(request.POST)
		if form.is_valid():
			username=form.cleaned_data['username']
			email=form.cleaned_data['email']
			password=form.cleaned_data['password']
			User.objects.create_user(username,email,password)
			return redirect('login')
	d['form']=user
	return render(request,'register.html',d)

@login_required
def project_view(request):
	d={}
	all_projects=	Projects.objects.all()
	d['projects']=all_projects
	# return redirect('projects')
	return render(request,'viwer.html',d)



@csrf_exempt
def login_user(request):
	d={}
	user=LoginForm()
	d['form']=user
	if request.method=='POST':
		form=LoginForm(request.POST)
		if form.is_valid():
			username=form.cleaned_data['username']
			password=form.cleaned_data['password']
			user = authenticate(username=username, password=password)
			if user is not None:
				d['name']=form.cleaned_data['username']
				login(request,user)
				return render(request,'profile1.html',d)
			else:
				return redirect('login')

	return render(request,'index.html',d)

@login_required
@csrf_exempt
def profile_view(request):
	# d={}
	# name=Students.objects.get('username')
	# print "hsac"
	# d['name']=name
	return render(request,'profile1.html',d)

def about_view(request):
	return render(request,'about.html')

def department_view(request):
	return render(request,'department.html')

def contact_view(request):
	return render(request,'contact.html')
