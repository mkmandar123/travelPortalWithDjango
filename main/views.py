from django.shortcuts import render
from .models import destination
# Create your views here.
context={}
def home(request):
	dest=destination.objects.all()
	context['dests']=dest
	return render(request,'index.html',context)