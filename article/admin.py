from django.contrib import admin
from .models import Article

from comment.models import Comment

class CommentInline(admin.TabularInline):
	model = Comment
	can_delete = False


class Articleadmin(admin.ModelAdmin):
	list_display = ('block', 'title', 'content', 'status', 'create_timestamp', 'last_update_timestamp')
	actions = ['make_picked']
	inlines = [CommentInline]
	fieldsets = (
		("基本", {"classes": ("",), "fields": ("title", "content")}),
		("高级", {"classes": ("collapse",), "fields": ("status", )})
	)
	readonly_fields = ("owner", "content", "status", "create_timestamp")

	def make_picked(self, request, queryset):
		for a in queryset:
			a.status = 10
			a.save()
	make_picked.short_description = '设置精华'


admin.site.register(Article, Articleadmin)
