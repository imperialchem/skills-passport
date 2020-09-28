from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),

    path('check_template', views.check_template, name='template_check'),

    path('student_drafts/', views.student_dafts_view, name='student_drafts'),
    # Initial page to create a draft
    path('new_draft/', views.create_draft, name='new_draft'),

    path('view_draft/<int:draft_id>', views.view_draft, name='view_draft')
    #Page to see current draft
]