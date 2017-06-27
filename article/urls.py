from django.conf.urls import url
from .views import article_list, ArticleCreateView
# from .views import articles_create

urlpatterns = [
	url(r'^list/(?P<block_id>\d+)', article_list),
	# #利用函数创建view
	# url(r'^create/(?P<block_id>\d+)', articles_create),
	#利用类创建view
	url(r'^create/(?P<block_id>\d+)', ArticleCreateView.as_view()),
]
