from django.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('postingan/<int:pk>/', views.post_detail, name='post_detail'),
    path('postingan/post_filter/', views.post_filter, name='post_filter'), 
    #crud postingan
    path('postingan/post_new/', views.post_new, name='post_new'),           
    path('postingan/<int:pk>/post_edit/', views.post_edit, name='post_edit'),
    path('postingan/<int:pk>/post_delete/', views.post_delete, name='post_delete'),
    #crud komentar        
    path('postingan/komen_new/', views.komen_new, name='komen_new'),
    path('postingan/<int:pk>/komen_edit/', views.komen_edit, name='komen_edit'),
    path('postingan/<int:pk>/komen_delete/', views.komen_delete, name='komen_delete'),
    #crud kategori
    path('postingan/kategori_list/', views.kategori_list, name='kategori_list'), 
    path('postingan/kategori_new/', views.kategori_new, name='kategori_new'),           
    path('postingan/<int:pk>/kategori_edit/', views.kategori_edit, name='kategori_edit'),
    path('postingan/<int:pk>/kategori_delete/', views.kategori_delete, name='kategori_delete'),
]