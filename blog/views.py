from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404



# Create your views here.
def index(request):
	print dir(request)
	print dir(request.user)
	print request.user.password
	return HttpResponse('test ok!')
