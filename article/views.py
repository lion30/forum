from django.shortcuts import render, redirect
from django.views.generic import View ,DetailView

from blocks.models import Block
from .forms import ArticleForm
from .models import Article
from comment.models import Comment
from utils.paginator import paginate_queryset


def article_list(request, block_id):
	block_id = int(block_id)
	blocks = Block.objects.get(id=block_id)
	page_no = int(request.GET.get('page_no','1'))
	all_articles = Article.objects.filter(block=blocks,status=0).order_by('-id')
	page_articles,pagination_data = paginate_queryset(all_articles, page_no)
	return render(request, 'article_list.html', {'blocks':blocks,
	                                             'articles':page_articles,
	                                             'pagination_data': pagination_data})



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
			article.owner = request.user
			article.status = 0
			article.save()
			return redirect('/article/list/%s' % block_id)
		else:
			return render(request, self.template_name, {'blocks': self.block, 'form': form})


# 利用函数创建文章详情页
# def article_detail(request, article_id):
# 	article_id = int(article_id)
# 	articles = Article.objects.filter(id=article_id)
# 	if request.method == 'GET':
# 		return render(request, 'article_detail.html', {'aids': articles})

class ArticleDetailView(DetailView):
	model = Article
	template_name = 'article_detail.html'
	context_object_name = 'article'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		page_no = int(self.request.GET.get('page_no', 1))
		all_comments = Comment.normal_objects.filter(article=context['article'])
		comments,pagination_data = paginate_queryset(all_comments, page_no, cnt_per_page=3)
		context['comments'] = comments
		context['pagination_data'] = pagination_data
		return context


