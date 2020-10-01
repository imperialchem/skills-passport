from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from .. import controllers
from ..models import Record

login_required()
@user_passes_test(controllers.is_student)
def student_dafts_view(request):

    drafts = Record.objects.filter(student_cid=request.user.profile.cid, state=0)
    final_statements = Record.objects.filter(student_cid=request.user.profile.cid, state=2)
    feedbacks = Record.objects.filter(student_cid=request.user.profile.cid, state=1)
    confirmations = Record.objects.filter(student_cid=request.user.profile.cid, state=3)


    template = 'chemtrack_app/students/see_drafts.html'
    context = {"drafts":drafts, "final_statements":final_statements, "feedbacks":feedbacks, "confirmations":confirmations}
    return render(request, template, context)