from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile,name='profile'),
    path('other_user/{?P<pk>\d+}',views.profile,name='profile_with_pk'),
    path('feedback/', views.feedback,name='feedback'),
    path('comment/{?P<pk>\d+}', views.postdetail,name='comment'),
    path('reply/{?P<pk>\d+}', views.create_reply,name='reply'),

    
]