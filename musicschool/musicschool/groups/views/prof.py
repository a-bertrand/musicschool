from django.views.generic import TemplateView


from  .models import MemberGroup, Media, Article

class ProfView(TemplateView):
    template_name = 'prof/home.html'

    def get(request):
        if request.user:
        if request.user.is_staff:
            return redirect('/admin')
        elif request.user.is_authenticated:
            try:
                membergroup =  request.user.members_group.all()[0]
            except:
                membergroup = None
            return render(
                request, 
                'home.html',
                {
                    'membergroup':membergroup,
                }
            )
        else:
            return redirect('login')
    else:
        return redirect('login')
