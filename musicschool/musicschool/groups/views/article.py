from django.views.generic import TemplateView
from  .models import MemberGroup, Media, Article

class ArticleView(TemplateView):
    template_name = "article/home.html"
    
    def get():
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