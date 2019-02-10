from django.shortcuts import redirect

def home_redirect(request):
    user_information = request.user.user_information
    if user_information.is_prof:
        return redirect('prof-home')
    else:
        return redirect('student-home')
    