from django.shortcuts import render_to_response, redirect
from django.contrib.auth.decorators import login_required

from .models import Usermessage


@login_required
def message_list(request):
	read_messages = Usermessage.objects.filter(owner=request.user, status=1).order_by("-id")
	unread_messages = Usermessage.objects.filter(owner=request.user, status=0).order_by("-id")
	return render_to_response("message_list.html", {"read_messages": read_messages,"unread_messages": unread_messages})


@login_required
def read_message(request,message_id):
	message = Usermessage.objects.get(id=int(message_id))
	message.status = 1
	message.save()
	return redirect(message.link)