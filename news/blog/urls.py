from django.contrib import admin
from django.urls import path, re_path

from blog.views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('about/', about, name='about'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('post/<slug:post_slug>', ShowPost.as_view(), name='post'),
    path('cats/<slug:cat>', categories),
    path('category/<int:cat_id>', show_category, name='category'),  #<slug:cat_slug>', PostCategory,as_view()
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive),
]
