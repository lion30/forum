from django import forms
from .models import Article


# class ArticleForm(forms.Form):
# 	article_title = forms.CharField(label='标题', max_length=100)
# 	article_content = forms.CharField(label='内容', max_length=10000)

# 直接从models里面引入数据
class ArticleForm(forms.ModelForm):
	class Meta:
		model = Article
		fields = ['title', 'content']