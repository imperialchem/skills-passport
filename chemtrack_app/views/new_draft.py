from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from .. import controllers


login_required()
@user_passes_test(controllers.is_student)
def create_draft(request):
    if request.method == 'GET':
        template = 'chemtrack_app/students/new_draft.html'
        context = {}
        return render(request, template, context)
    elif request.method == 'POST':
        pass
    else:
        return redirect('/')