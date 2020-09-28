from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from ..models import Record
from .. import controllers
from django import forms


login_required()
@user_passes_test(controllers.is_student)
def view_draft(request, draft_id=-1):
    # If no id are in the url
    if draft_id == -1:
        if controllers.is_student(request.user):
            return redirect('student_drafts')
        else:
            return redirect('/')
    else:
        template = 'record_management/draft.html'

        draft=  Record.objects.filter(pk=draft_id)

        context = {"record":draft}
        return render(request, template, context)