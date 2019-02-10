from django.views.generic import View
from musicschool.groups.models import MemberGroup, Media, Article
from django.shortcuts import redirect, render
from django.contrib.auth.models import User


class ArticleView(View):
    template_name = "article/home.html"
    
    def get(self, request, article_id):
        try:
            if User.is_authenticated:   
                article = Article.objects.get(pk=article_id)
                membergroup =  request.user.members_group.all()[0]
                if article in membergroup.articles.all():
                    return render(
                        request, 
                        'article_detail.html', 
                        {
                            'article':article, 
                            'medias': article.media.all()
                        }
                    ) 
                else:
                    return render(request, 'layout/not_right_page.html')
            else:
                return redirect('login')
        except:
            return redirect('login')