from musicschool.libs.logged_view import LoggedView

class LoggedView(LoggedView):
    def dispatch(self, *args, **kwargs):
        if request.user.is_authenticated:
            return super(LoggedView, self).dispatch(*args, **kwargs)
        else:
            return redirect('login')


class ProfView(LoggedView):
    def dispatch(self, *args, **kwargs):
        if request.user.is_authenticated:
            return super(LoggedView, self).dispatch(*args, **kwargs)
        else:
            return redirect('login')


class StudentView(LoggedView):
    def dispatch(self, *args, **kwargs):
        if request.user.is_authenticated:
            return super(LoggedView, self).dispatch(*args, **kwargs)
        else:
            return redirect('login')
