# Generated by Django 3.0.5 on 2020-09-28 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chemtrack_app', '0005_auto_20200904_1721'),
    ]

    operations = [
        migrations.RenameField(
            model_name='record_category',
            old_name='record_id',
            new_name='record',
        ),
        migrations.RenameField(
            model_name='record_category',
            old_name='template_id',
            new_name='template',
        ),
        migrations.RenameField(
            model_name='record_descriptor',
            old_name='category_id',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='record_descriptor',
            old_name='template_id',
            new_name='template',
        ),
    ]