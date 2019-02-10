from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path, include
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views

from musicschool.groups.views import (
    ArticleView,
    home_redirect,
    ProfView,
    StudentView,
    RegistrationView
)

urlpatterns = [
	path('', auth_views.LoginView.as_view(), name="login"),
    path('admin/', admin.site.urls, name='admin'),
    path('accounts/register', RegistrationView.as_view(), name='register'),
    path('home', home_redirect, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    ###############################################################
    # student
    path('student/home/', StudentView.as_view(), name='student-home'),
    # prof
    path('prof/home', ProfView.as_view(),name='prof-home'),
    ###############################################################
    # articles 
    path('article/<int:article_id>/', ArticleView.as_view(), name='article-detail'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)