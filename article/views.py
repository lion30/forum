from django.shortcuts import render, redirect
from blocks.models import Block
from .models import Article
from .forms import ArticleForm
from django.views.generic import View


def article_list(request, block_id):
	block_id = int(block_id)
	block = Block.objects.filter(id=block_id)
	article_objs = Article.objects.filter(block=block, status=0).order_by('-id')
	return render(request, 'article_list.html', {'articles': article_objs, 'blocks': block})


# def articles_create(request, block_id):
# 	block_id = int(block_id)
# 	block = Block.objects.filter(id=block_id)
# 	print('block_id=', block_id)
# 	print('block=',block)
# 	if request.method == 'GET':
# 		return render(request, 'create.html', {'blocks': block})
# 	else:
# 		title = request.POST['title'].strip()
# 		content = request.POST['content'].strip()
# 		#简单的页面校验功能
# 		# if not article_title or not article_content:
# 		# 	return render(request, 'create.html',{'blocks': block, 'error': '标题或内容不能为空！', 'article_title': article_title, 'article_content': article_content})
# 		# if len(article_title)>100 or len(article_content)>10000:
# 		# 	return render(request, 'create.html', {'blocks': block, 'error': '标题或内容太长！', 'article_title': article_title, 'article_content': article_content})
# 		# article = Article(block_id=block_id, title=article_title, content=article_content, status=0)
# 		# article.save()
# 		# return redirect('/article/list/%s' % block_id)
# 		#利用forms的校验
# 		form = ArticleForm(request.POST)
# 		if form.is_valid():
# 			# article = Article(block_id=block_id, title=form.cleaned_data['title'], content=form.cleaned_data['content'], status=0)
# 			# article.save()
# 			# return redirect('/article/list/%s' % block_id)
# 		# # 换一种方法实现,减少字段输入
# 			article = form.save(commit=False)
# 			article.block_id = block_id
# 			article.status = 0
# 			article.save()
# 			return redirect('/article/list/%s' % block_id)
# 		else:
# 			return render(request, 'create.html', {'blocks': block, 'form': form})


# 类的实现
class ArticleCreateView(View):

	template_name = 'create.html'

	def init_data(self, block_id):
		self.block_id = int(block_id)
		self.block = Block.objects.filter(id=self.block_id)

	def get(self, request, block_id):
		# #提取成init_data
		# block_id = int(block_id)
		# block = Block.objects.filter(id=block_id)
		self.init_data(block_id)
		return render(request, self.template_name, {'blocks': self.block})

	def post(self, request, block_id):
		# #下面两行代码get函数也有，因此需进行提取
		# block_id = int(block_id)
		# block = Block.objects.filter(id=block_id)
		self.init_data(block_id)
		form = ArticleForm(request.POST)
		if form.is_valid():
			article = form.save(commit=False)
			article.block_id = self.block_id
			article.status = 0
			article.save()
			return redirect('/article/list/%s' % block_id)
		else:
			return render(request, self.template_name, {'blocks': self.block, 'form': form})


# 利用函数创建文章详情页
def article_detail(request, article_id):
	article_id = int(article_id)
	articles = Article.objects.filter(id=article_id)
	if request.method == 'GET':
		return render(request, 'article_detail.html', {'aids': articles})