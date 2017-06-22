from django.shortcuts import render
from blocks.models import Block


def htmltemplate(request):
	return render(request, "htmltemplate.html")


def index(request):
	block_infos = Block.objects.all().filter(status=0).order_by('-id')
	return render(request, "index.html",{'blocks':block_infos})
