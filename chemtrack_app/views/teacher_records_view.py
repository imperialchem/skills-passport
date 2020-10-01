from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from .. import controllers
from ..models import Record, Assignment

login_required()
@user_passes_test(controllers.is_teacher)
def teacher_records_view(request):

    student_cids = Assignment.objects.filter(teacher=request.user).values_list('student', flat=True)

    feedback = Record.objects.filter(student__in=student_cids, state=1)
    confirmation = Record.objects.filter(student__in=student_cids, state=3)


    template = 'chemtrack_app/teachers/see_records.html'
    context = {"feedback":feedback, "confirmation":confirmation}
    return render(request, template, context)