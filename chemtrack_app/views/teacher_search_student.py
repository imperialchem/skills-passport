from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from .. import controllers
from ..models import Record, Profile

login_required()
@user_passes_test(controllers.is_teacher)
def teacher_search_student(request):
    drafts = []
    final_statements = []
    feedbacks = []
    confirmations = []
    records = []
    search = False
    found = False
    cid = ""
    student = None

    if "student_cid" in request.GET:
        student = Profile.objects.filter(cid=request.GET["student_cid"])
        search = True
        cid = request.GET["student_cid"]
        if len(student) == 1:
            student = student[0].user

            drafts = Record.objects.filter(student=student, state=0)
            final_statements = Record.objects.filter(student=student, state=2)
            feedbacks = Record.objects.filter(student=student, state=1)
            confirmations = Record.objects.filter(student=student, state=3)
            records = Record.objects.filter(student=student, state=4)
            found = True

    template = 'chemtrack_app/teachers/teacher_search_student.html'
    context = {"student":student, "records":records, "search":search, "found":found, "drafts":drafts, "final_statements":final_statements, "feedbacks":feedbacks, "confirmations":confirmations}
    return render(request, template, context)