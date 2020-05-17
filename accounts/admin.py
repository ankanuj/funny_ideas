from django.contrib import admin
from .models import Profile,Post,Feedback,Comment,Debate

class ProfileAdmin(admin.ModelAdmin):
	list_display=('id','user','date','is_published')
	list_display_links=('id','user','is_published')
	list_filter = ('user',)
	search_fields = ('user',)
	list_per_page = 25

admin.site.register(Profile,ProfileAdmin)

class PostAdmin(admin.ModelAdmin):
	list_display=('id','user','date','is_published')
	list_display_links=('id','user','is_published')
	list_filter = ('user',)
	search_fields = ('user',)
	list_per_page = 25

admin.site.register(Post,PostAdmin)

class FeedbackAdmin(admin.ModelAdmin):
	list_display=('id','user','date',)
	list_display_links=('id','user',)
	list_filter = ('user',)
	search_fields = ('user',)
	list_per_page = 25

admin.site.register(Feedback,FeedbackAdmin)

class CommentAdmin(admin.ModelAdmin):
	list_display=('id','user','post','com_date','reply','is_published')
	list_display_links=('id','user','post')
	list_filter = ('user','post')
	search_fields = ('user','post')
	list_per_page = 25

admin.site.register(Comment,CommentAdmin)


class DebateAdmin(admin.ModelAdmin):
	list_display=('id','user','topic','com_date','is_published')
	list_display_links=('id','user','topic')
	list_filter = ('user','topic')
	search_fields = ('user','topic')
	list_per_page = 25

admin.site.register(Debate,DebateAdmin)