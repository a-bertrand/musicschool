from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path, include
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views

from musicschool.groups.views import (
    ProfView,
    StrudentView
)



urlpatterns = [
	path('', auth_views.LoginView.as_view()),
    path('admin/', admin.site.urls, name='admin'),
    path('accounts/register',groups_views.signup, name='register'),
    path('home',groups_views.home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    ###############################################################
    # student
    path('student/', ,name='student-home')),
    # prof
    path('prof/home', ,name='prof-home'),
    ###############################################################
    # articles 
    path('article/<int:article_id>/', groups_views.detail, name='article-detail'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)