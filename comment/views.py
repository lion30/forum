from django.shortcuts import render
from utils.responses import json_response

from article.models import Article
from comment.models import Comment
from message.models import Usermessage


def create_comment(request):
	if not request.user.is_authenticated():
		return json_response({'status':'error', 'msg':'您没有登陆，不能发表评论哦'})
	article_id = int(request.POST["article_id"])
	to_comment_id = int(request.POST.get('to_comment_id', 0))
	content = request.POST['content'].strip()

	if not content:
		return json_response({'status':'error', 'msg':'评论内容不能为空'})
	article = Article.objects.get(id=article_id)

	if to_comment_id != 0:
		to_comment = Comment.objects.get(id=to_comment_id)
		new_msg = Usermessage(owner=to_comment.owner, content='有人回复了你的评论‘%s’'% to_comment.content[:30],
		                      link="http://%s/article/articledetail/%s"%(request.get_host(),article_id))
		new_msg.save()
	else:
		to_comment = None
		new_msg = Usermessage(owner=article.owner,
		                      content="有人评论了你的文章《%s》"%article.title,
		                      link="http://%s/article/articledetail/%s"%(request.get_host(),article.id))
		new_msg.save()
	comment = Comment(article=article,owner=request.user,content=content,to_comment=to_comment)
	comment.save()
	return json_response({'status':'ok', 'msg':''})