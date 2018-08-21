from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
	return render(request, 'homepage.html', {})


def home_page_old(request):
	return HttpResponse('ksjdf')