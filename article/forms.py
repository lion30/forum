from django import forms

from .models import Article


# 直接从models里面引入数据
class ArticleForm(forms.ModelForm):
	class Meta:
		model = Article  # Artilce数据表
		fields = ['title', 'content']  # Article数据表中
