from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile,name='profile'),
    path('other_user/{?P<pk>\d+}',views.profile,name='profile_with_pk'),
    path('feedback/', views.feedback,name='feedback'),
    path('comment/{?P<pk>\d+}', views.postdetail,name='comment'),
    path('reply/{?P<pk>\d+}', views.create_reply,name='reply'),
    path('edit/post/{?P<pk>\d+}',views.edit_post,name="edit_post"),
    path('delete/post/{?P<pk>\d+}',views.delete_post,name="delete_post"),
    path('edit/debate/{?P<pk>\d+}',views.edit_debate,name="edit_debate"),
    path('delete/debate/{?P<pk>\d+}',views.delete_debate,name="delete_debate"),
    



    
]