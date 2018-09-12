from django.contrib.auth import authenticate, login, get_user_model

from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm


def home_page(request):
	#print(request.session.get("first_name", "Unknown"))
	context = {
		"title": "Hello World",
		"content": "Welcome to the homepage."
	}
	if request.user.is_authenticated:
		context['premium_content'] = "You already have loged in"
	return render(request, 'homepage.html', context)

def about_page(request):
	context = {
		"title": "About Page",
		"content": "Welcome to the about page."
	}
	return render(request, 'homepage.html', context)

def contact_page(request):
	contact_form = ContactForm(request.POST or None)
	context = {
		"title": "Contact Page",
		"content": "Welcome to contact page.",
		"form": contact_form
	}
	if contact_form.is_valid():
		print(contact_form.cleaned_data)

	# if request.method == 'POST':
	# 	print(request.POST.get('fullname'))
	# 	print(request.POST.get('email'))
	# 	print(request.POST.get('content'))
	return render(request, 'homepage.html', context)


def home_page_old(request):
	return HttpResponse('ksjdf')


	