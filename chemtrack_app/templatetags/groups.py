from django.contrib.auth.models import Group
from django import template


register = template.Library()

@register.filter(name='has_group')
def has_group(user, group_name):
    print(user.groups.all())
    return user.groups.filter(name=group_name).exists()