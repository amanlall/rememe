from django.urls import path, include
from . views import PostListView , PostCreateView, PostDetailView, PostUpdateView, PostDeleteView
from . import views


urlpatterns = [
   path('', PostListView, name="blog-home"),
   path('post/<int:pk>/', views.PostDetailView, name="post-detail"),
   #path('post/new/', PostCreateView.as_view(), name="post-create"),
   path('allrememers', views.RememerList, name="rememer-list"),
   path('post/', views.photo_list, name="post-create"),
   path('post/<int:pk>/update', PostUpdateView.as_view(), name="post-update"),
   path('post/<int:pk>/delete', PostDeleteView.as_view(), name="post-delete"),
   path('contact/', views.contact, name="contact"),
   #path('post/<user>', views.contact, name="memer"),
]

