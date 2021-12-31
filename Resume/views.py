from django.shortcuts import render
from .models import Add_project

# Create your views here.

def home(request):
	add_project = Add_project.objects.all()

	return render(request,'index.html',{'add_project':add_project})