from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),

    path('check_template', views.check_template, name='template_check'),

    path('student_drafts/', views.student_dafts_view, name='student_drafts'),

    path('student_records/', views.student_records_view, name='student_records'),

    path('teacher_records/', views.teacher_records_view, name='teacher_records'),

    path('search_student/', views.teacher_search_student, name='search_student'),
    # Initial page to create a draft
    path('new_draft/', views.create_draft, name='new_draft'),
    # Main page, modifying drafts
    path('view_record/<int:record_id>', views.view_record, name='view_record'),

    # Backend to modify level in DB
    path('ajax/update_level', views.update_level, name='update_level'),

    path('ajax/update_statement', views.update_statement, name='update_statement')
]