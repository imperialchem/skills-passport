from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from .. import controllers
from ..models import Record

login_required()
@user_passes_test(controllers.is_student)
def student_dafts_view(request):

    records = Record.objects.filter(student_cid=request.user.profile.cid)


    template = 'chemtrack_app/students/see_drafts.html'
    context = {"records":records}
    return render(request, template, context)