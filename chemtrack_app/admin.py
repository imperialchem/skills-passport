from django.contrib import admin

from .models import Assignment, Category_template, Descriptor_template, Record, Record_category, Record_descriptor, Profile

admin.site.register(Assignment)
admin.site.register(Category_template)
admin.site.register(Descriptor_template)
admin.site.register(Record)
admin.site.register(Record_category)
admin.site.register(Record_descriptor)
admin.site.register(Profile)