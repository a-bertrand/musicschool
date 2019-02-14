from django.views.generic import View

class LoggedView(View):
    def dispatch(self, *args, **kwargs):
        if request.user.is_authenticated:
            return super(LoggedView, self).dispatch(*args, **kwargs)
        else:
            return redirect('login')


class LoggedProfView(LoggedView):
    def dispatch(self, *args, **kwargs):
        if request.user.is_authenticated and request.user.user_information.is_prof:
            return super(LoggedView, self).dispatch(*args, **kwargs)
        else:
            return redirect('login')


class LoggedStudentView(LoggedView):
    def dispatch(self, *args, **kwargs):
        if request.user.is_authenticated:
            return super(LoggedView, self).dispatch(*args, **kwargs)
        else:
            return redirect('login')
