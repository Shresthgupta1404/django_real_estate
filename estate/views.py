from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import desc
from .serializer import modescserializers

def signin_form(request):
	"""
	desc: this func render's the login page
	author: shresth
	:param request:request
	:return:render
	:Method allowed: GET
	"""
	return render(request,'tab-2.html')


def signin_check(request):
	"""
	desc: this function autrhnticate thr user
	author: shresth
	:param request: request
	:return: Redirect
	:Method allowed: POST
	"""
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			print("user exists")
			return render(request,'home.html')
		else:
			print("User does not exists")
			return HttpResponseRedirect('/signin')

def sign_up(request):
	"""
	desc: this func render's the signup page
	author: shresth 
	:param request: request
	:return: render
	:Method allowed: GET
	"""
	return render(request,'index.html')

def home(request):
	"""
	desc: this func render's the signup page
	author: shresth 
	:param request: request
	:return: render
	:Method allowed: GET
	"""
	return render(request,'home.html')

def create_user(request):
	"""
	desc: takes the input from the signup page and creates the user account
	author: shresth 
	:param request: request
	:Method allowed: POST
	"""
	if request.method == "POST":
		fullname = request.POST['fullname']
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		try:
			User.objects.create_user(username, email, password)
			print("user created")
			return HttpResponseRedirect('tab2')
		except Exception as e:
			print("user already exists")
			return HttpResponseRedirect('tab2')



def uploadPics(request):
	if request.method=="POST":
		killer = modescserializers(keyword=request.POST['keyword'],types=request.POST['types'],city=request.POST['city'],	bedrooms=request.POST['bedrooms'],garages=request.POST['garages'],price=request.POST['price'])
		killer.is_valid()
		killer.save()
		
	else:
		print("Get request",end='\n\n\n')
	return render(request,'pic.html')


def about(request):
	return render(request,'about.html')


def property(request):
	return render(request,'property-grid.html')

def propertysingle(request):
	return render(request,'property-single.html')

def contact(request):
	return render(request,'contact.html')

def bloggrid(request):
	return render(request,'blog-grid.html')	

def blogsingle(request):
	return render(request,'blog-single.html')	

def tab2(request):
	return render(request,'tab-2.html')