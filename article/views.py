from django.shortcuts import render, redirect
from blocks.models import Block
from .models import Article


def article_list(request, block_id):
	block_id = int(block_id)
	block = Block.objects.filter(id=block_id)
	article_objs = Article.objects.filter(block=block, status=0).order_by('-id')
	return render(request, 'article_list.html', {'articles': article_objs, 'blocks': block})


def articles_create(request, block_id):
	block_id = int(block_id)
	block = Block.objects.filter(id=block_id)
	if request.method == 'GET':
		return render(request, 'create.html', {'blocks': block})
	else:
		article_title = request.POST['article_title'].strip()
		article_content = request.POST['article_content'].strip()
		if not article_title or not article_content:
			return render(request, 'create.html',{'blocks': block, 'error': '标题或内容不能为空！', 'article_title': article_title, 'article_content': article_content})
		if len(article_title)>100 or len(article_content)>10000:
			return render(request, 'create.html', {'blocks': block, 'error': '标题或内容太长！', 'article_title': article_title, 'article_content': article_content})
		article = Article(block_id=block_id, title=article_title, content=article_content, status=0)
		article.save()
		return redirect('/article/list/%s' % block_id)
