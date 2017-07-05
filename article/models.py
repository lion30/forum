from django.contrib.auth.models import User
from django.db import models
from blocks.models import Block
import pytz

BEIJING_TZ = pytz.timezone('Asia/Shanghai')

class Article(models.Model):
	owner = models.ForeignKey(User, verbose_name='作者')
	block = models.ForeignKey(Block, verbose_name='版块ID')
	title = models.CharField('模块名称', max_length=100)
	content = models.CharField('模块描述', max_length=100)
	status = models.IntegerField('状态', choices=((0, '正常'), (1, '删除')))

	create_timestamp = models.DateTimeField('创建时间', auto_now_add=True)
	last_update_timestamp = models.DateTimeField('修改时间', auto_now=True)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = '文章'
		verbose_name_plural = '文章'
