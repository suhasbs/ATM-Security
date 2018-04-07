# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from .models import *
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def test(request):

	return JsonResponse({'resp':"Hello there"})


@csrf_exempt
def uploadImage(request):
	print request.META['CONTENT_TYPE']
	if request.method == 'GET':
		return render(request, 'AtmSecurity/file_upload.html')
	if request.method=='POST':
		print request.POST, request.FILES
		instance = ImageUpload(image=request.FILES['image_file'])
		instance.status = 0
		instance.save()
		request.session['new_images'] = True
		return render(request, 'AtmSecurity/file_upload.html')


def sendImage(request):
	if 'new_images' in request.session and request.session['new_images']:
		new_images = ImageUpload.objects.filter(status=0)
		for image in new_images:
			image.status=1
			image.save()

