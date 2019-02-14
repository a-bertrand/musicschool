from groups.models import Group

"""
    redirect if teacher or user 
"""
def home_redirect(request):
    user_information = request.user.user_information
    if request.user.user_information.is_prof:
        return redirect('prof-home')
    else
        return redirect('student-home')
    