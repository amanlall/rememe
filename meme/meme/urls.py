"""meme URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views
from django.contrib.auth import views as auth_views
from blog import views as blog_views

#urlpatterns = [
    # ... the rest of your URLconf goes here ...
#] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns = [
    #path('', include('memeapp.urls')),
    path('', include('blog.urls')),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/' ,auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('admin/', admin.site.urls),
    path('profile/', user_views.profile, name='profile'),
    path('memer/<slug:slugs>/', blog_views.ProfileDetailView, name='memer-profile'),
    path('like/', blog_views.like_post, name="like_post"),
    path('sitemap/', blog_views.sitemap, name="sitemap"),

    
]
#if settings.DEBUG:
#    urlpatterns= urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

