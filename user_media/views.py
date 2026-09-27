from django.shortcuts import render
from django.http import HttpResponse

def hello_world(request):
	return HttpResponse('Hello, World!<br><br>This is the root page of NerdHoard!')
