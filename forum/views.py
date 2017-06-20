from django.shortcuts import render


def htmltemplate(request):
	return render(request, "htmltemplate.html")


def index(request):
	return render(request, "index.html")
