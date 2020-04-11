
from django.contrib import admin
from django.urls import path,include
from accounts.views import index,about,logout
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='home'),
    path('about',about,name='about'),
    path('logout',logout,name='logout'),
    path('accounts/', include('accounts.urls')),
    path('accounts/',include('allauth.urls')),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)