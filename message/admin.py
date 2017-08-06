from django.contrib import admin

# Register your models here.
from .models import Usermessage


class UserMessageAdmin(admin.ModelAdmin):
	list_display = ("owner","content","status","create_timestamp","last_update_timestamp")
	search_fields = ["content"]
	list_filter = ("status", )

admin.site.register(Usermessage, UserMessageAdmin)