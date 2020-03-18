from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import auth,User

# Create your views here.
def login(request):
	return render(request,'login.html')

def signin(request):
	
		username=request.POST['username']
		password=request.POST['pass']
		user=auth.authenticate(username=username,password=password)
		if user:
			return render(request,'index.html',{'user':user})
		else:
			return HttpResponse("FAILED")
	
def logout(request):
	auth.logout(request)
	return render(request,'index.html')