from django.contrib import admin
from .models import Profile,Post,Feedback

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