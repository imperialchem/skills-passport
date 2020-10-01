#
# Function that checks whether the json template provided is valid with what
# is in the database
#       Checks that the categories exist
#       Checks that the descriptors exist
#
#
import json
from django.conf import settings
from ..models import Category_template, Descriptor_template


def check_template():
    result = True
    err = ""
    with open(settings.TEMPLATE_RECORD, "r") as file:

        data = json.load(file)

        for category in data["categories"]:

            # if the category is not in the database
            if not Category_template.objects.filter(pk=category["id"]).exists():
                result = False
                err += f"Invalid category id {category['id']} <br/>"

            # If a descriptor for this category is missing
            if not (Descriptor_template.objects.filter(pk__in=category["descriptors"]).count() == len(category["descriptors"])):
                result = False
                err += f"Invalid descriptor id in {category['descriptors']} <br/>"


    return result, err

def get_template():
    with open(settings.TEMPLATE_RECORD, "r") as file:

        data = json.load(file)
        result = []

        for category_id in data["categories"]:

            # if the category is not in the database
            category = Category_template.objects.filter(pk=category_id["id"])[0]

            descriptors = []
            for desc_id in category_id["descriptors"]:
                desc = Descriptor_template.objects.filter(pk=desc_id)[0]
                descriptors.append(desc)

            result.append({"category":category, "descriptors":descriptors})


    return result
