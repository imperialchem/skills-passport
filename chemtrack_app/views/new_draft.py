from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from .. import controllers
from django import forms


class NewDarftForm(forms.Form):
    name = forms.CharField(required=True)
    description = forms.CharField(required = False)
    date = forms.DateField(required=True)


login_required()
@user_passes_test(controllers.is_student)
def create_draft(request):

    if request.method == 'GET':
        template = 'chemtrack_app/students/new_draft.html'
        context = {}
        return render(request, template, context)
    elif request.method == 'POST':
        form = NewDarftForm(request.POST)
        print(request.POST)
        print(form.errors)
        if form.is_valid():
            new_id = controllers.create_record(request.user.profile.cid, form.cleaned_data["name"], form.cleaned_data["description"], form.cleaned_data["date"])
            return redirect(f'view_record/{new_id}')

        else:
            return redirect('new_draft')
    else:
        return redirect('/')
