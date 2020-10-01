from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from ..models import Record
from .. import controllers
from django import forms


login_required()
def view_record(request, record_id=-1):
    # If no id are in the url
    record=  Record.objects.filter(pk=record_id)

    if len(record) != 1 or not controllers.has_acces_to(record[0], request.user):
        if controllers.is_student(request.user):
            return redirect('student_drafts')
        else:
            return redirect('/')
    else:
        # If the record does exist
        record = record[0]

        if "submit_record" in request.POST:
            if (record.state == 0 or record.state == 2) and controllers.is_student(request.user):
                record.state += 1
                record.save()
            elif (record.state == 1 or record.state == 3) and controllers.is_teacher(request.user):
                record.state += 1
                record.save()

            return redirect("view_record", record_id=record_id)

        elif "delete_record" in request.POST:
            if record.state == 0 and controllers.is_student(request.user):
                record.delete()
                return redirect("student_drafts")
            else:
                return redirect("view_record", record_id = record.pk)

        elif "modify_state" in request.POST and "new_state" in request.POST and controllers.is_teacher(request.user):
            new_state = int(request.POST["new_state"])
            if new_state >= 0 and new_state <= 4:
                record.state = new_state
                record.save()


            return redirect("view_record", record_id=record_id)
        else:
            if "page" in request.GET and request.GET["page"] == "admin":
                template = 'chemtrack_app/record_management/admin.html'

                context = {"record":record}
                return render(request, template, context)


            else:
                template = 'chemtrack_app/record_management/record.html'


                context = {"record":record}
                return render(request, template, context)