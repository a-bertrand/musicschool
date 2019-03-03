from django.forms import ModelForm
from .models import (
    Article,
    Category,
    Media,
    MemberGroup,
    ERPUser,
)


class ArticleForm(ModelForm):
    class Meta: 
        model = Article
        fields = '__all__'


class UserForm(ModelForm):
    class Meta: 
        model = ERPUser
        fields = '__all__'


class MediaForm(ModelForm):
    class Meta: 
        model = Media
        fields = '__all__'
