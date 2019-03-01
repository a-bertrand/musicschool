from django.forms import ModelForm
from .models import (
    Article,
    Media,
    MemberGroup,
    Category
)


class ArticleForm(ModelForm):

    class Meta: 
        model = Article
        fields = '__all__'