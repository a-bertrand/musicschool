from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path, include
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views

from musicschool.groups.views import (
    ArticleDetailView,
    ArticleListView,
    ArticleManageView,
    ArticleDeleteView,
    home_redirect,
    ProfView,
    StudentView,
    RegistrationView
)

urlpatterns = [
	path('', auth_views.LoginView.as_view(), name="login"),
    path('admin/', admin.site.urls, name='admin'),
    path('accounts/register/', RegistrationView.as_view(), name='register'),
    path('home', home_redirect, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),

    ###############################################################
    # student
    path('student/home/', StudentView.as_view(), name='student-home'),
    # prof
    path('prof/home/', ProfView.as_view(),name='prof-home'),

    ###############################################################
    # articles 
    path('article/<int:article_id>/', ArticleDetailView.as_view(), name='article-detail'),
    path('article/list/', ArticleListView.as_view(), name='article-list'),
    path('article/<int:article_id>/edit/', ArticleManageView.as_view(), name='article-edit'),
    path('article/add/', ArticleManageView.as_view(), name='article-add'),
    path('article/<int:article_id>/del/', ArticleDeleteView.as_view(), name='article-del')

    ###############################################################
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)