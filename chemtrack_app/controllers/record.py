from ..models import Record, Record_category, Record_descriptor
from django.utils import timezone
import json
from django.conf import settings

#   Helper function that creates new records based on the current template
#
#


def create_record(student_cid):
    """

    :param student_cid: string : CID of the student
    :return: id of new record
    """
    new_record = Record(date_creation=timezone.now(), student_cid=student_cid)
    new_record.save()


    with open(settings.TEMPLATE_RECORD, "r") as file:

        template = json.load(file)

        for category in template["categories"]:

            new_category = Record_category(template_id=category["id"], record_id=new_record.pk)
            new_category.save()

            for descriptor_id  in category["descriptors"]:

                new_descriptor= Record_descriptor(template_id=descriptor_id, category_id=new_category.pk)
                new_descriptor.save()

    return True

