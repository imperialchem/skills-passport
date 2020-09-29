from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from ..models import Record
from .. import controllers
from django import forms


login_required()
@user_passes_test(controllers.is_student)
def view_record(request, record_id=-1):
    # If no id are in the url
    if record_id == -1:
        if controllers.is_student(request.user):
            return redirect('student_drafts')
        else:
            return redirect('/')
    else:
        template = 'chemtrack_app/record_management/record.html'

        record=  Record.objects.filter(pk=record_id)
        context = {"record":record[0]}
        return render(request, template, context)