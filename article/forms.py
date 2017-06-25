from django import forms


class ArticleForm(forms.Form):
	article_title = forms.CharField(label='标题', max_length=100)
	article_content = forms.CharField(label='内容', max_length=10000)
