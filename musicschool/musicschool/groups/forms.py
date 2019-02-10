from django.forms import ModelForm

import .models from (
    Article,
    Media,
    MemberGroup,
    Category,
    UserInformations
)


class ArticleForm(ModelForm):
    class Meta: 
        model = Article


class MediaForm(ModelForm):
    class Meta:
        model = Media


class MemberGroupForm(ModelForm):
    class Meta:
        model = MemberGroup


class CategoryForm(ModelForm):
    class Meta:
        model = Category


class UserInformationsForm(ModelForm):
    class Meta: 
        model = UserInformations
