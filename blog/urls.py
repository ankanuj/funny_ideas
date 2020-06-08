
from django.contrib import admin
from django.urls import path,include
from accounts.views import index,about,logout,debate,debate_details
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='home'),
    path('about/',about,name='about_us'),
    path('logout',logout,name='logout'),
    path('debate/',debate,name='debate'),
    path('debate/topic/online_classes',debate_details,name='debate_details_1'),
    path('debate/topic/tour_of_duty',debate_details,name='debate_details_2'),
    path('debate/topic/extend_lockdown',debate_details,name='debate_details_3'),
    path('accounts/', include('accounts.urls')),
    path('accounts/',include('allauth.urls')),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)