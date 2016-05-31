from django import forms
from Students.models import Students,Projects

# from students.models import user_login

class UserAddForm(forms.ModelForm):
	class Meta:
		model=Students
		fields=['username', 'email', 'password']


class StudentAddForm(forms.Form):
	# class Meta:
	# 	model=Projects
	# 	fields=['Projectname', 'Projectyear', 'Branch','Projectdescription']
		Projectname=forms.CharField(max_length=1000)
		Projectyear=forms.IntegerField()
		Branch=forms.CharField(max_length=30) 
		Projectdescription=forms.CharField(max_length=5000) 

class LoginForm(forms.Form):
	username=forms.CharField()
	password=forms.CharField(max_length=30,widget=forms.PasswordInput)

class UserForm(forms.ModelForm):
	class Meta:
		model=Students
		fields = "__all__" 
		widgets={
		'password':forms.PasswordInput()
		}