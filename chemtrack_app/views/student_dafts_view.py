from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from .. import controllers


login_required()
@user_passes_test(controllers.is_student)
def student_dafts_view(request):
    template = 'chemtrack_app/students/see_drafts.html'
    context = {}
    return render(request, template, context)