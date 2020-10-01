from ..models import Record, Record_category, Record_descriptor, Descriptor_template, Category_template
from django.utils import timezone
import json
from django.conf import settings
from .templates import get_template
from .groups import is_teacher, is_student

#   Helper function that creates new records based on the current template
#
#

def create_record(student_cid, name, description, date):
    """

    :param student_cid: string : CID of the student
    :return: id of new record
    """
    new_record = Record(date_creation=timezone.now(), student_cid=student_cid, name=name, description=description, date=date)
    new_record.save()


    template = get_template()


    for category in template:
        new_category = Record_category(template=category["category"], record=new_record)
        new_category.save()

        for descriptor  in category["descriptors"]:

            new_descriptor= Record_descriptor(template=descriptor, category=new_category)
            new_descriptor.save()




    return new_record.pk

def has_acces_to(record, user):
    if is_teacher(user):
        return True
    elif is_student(user) and record.student_cid == user.profile.cid:
        return True
    else:
        return False

def can_modify(record, user, state):
    """
        Function that decides if the user can modify a specific field
            Teacher can modify only feedback
            Students can modify Drafts and Final statements

        state is the state of the field of the descriptor considered:
            0:Draft
            1:FeedBack
            2:Final
    """
    if has_acces_to(record, user):
        if is_teacher(user) and state == 1 and record.state == 1:
            return True
        elif is_student(user) and state == 0 and record.state == 0:
            return True
        elif is_student(user) and state == 2 and record.state == 2:
            return True
    return False

def can_submit(record, user):
    result = False
    if record.state == 0 or record.state == 2:
        if is_student(user):
            result = True
    elif record == 1 or record.state == 3:
        if is_teacher(user):
            result = True
    return result