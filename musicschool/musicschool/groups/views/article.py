from musicschool.libs.logged_view import LoggedProfView
from musicschool.groups.models import MemberGroup, Media, Article
from django.shortcuts import redirect, render
from django.contrib.auth.models import User



def user_is_prof_and_auth():
    return True
    return False

# Detail 
class ArticleDetailView(LoggedStuddentView):
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


# List 
class ArticleListView(LoggedProfView):
    template_name = "prof/article_add_edit.html"
    
    def get(self, request):
        article = Article.objects.all()
        return render(
            request, 
            self.template_name, 
            {
                'articles':articles
            }
        ) 


#Edit - add
class ArticleManageView(View):
    template_name = "prof/article_add_edit.html"
    
    def get(self, request, article_id):
        article = Article.objects.get(pk=article_id)
        return render(
            request, 
            'article_detail.html', 
            {
                'article':article, 
                'medias': article.media.all()
            }
        ) 
