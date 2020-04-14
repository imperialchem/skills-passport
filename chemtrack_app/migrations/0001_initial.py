# Generated by Django 3.0.5 on 2020-04-14 09:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_cid', models.CharField(max_length=15)),
                ('teacher_cid', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Category_template',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Descriptor_template',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('order', models.IntegerField(default=0)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chemtrack_app.Category_template')),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('student_cid', models.CharField(max_length=15)),
                ('state', models.IntegerField(default=0)),
                ('levels', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Record_category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField(default=0)),
                ('record_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chemtrack_app.Record')),
                ('template_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chemtrack_app.Category_template')),
            ],
        ),
        migrations.CreateModel(
            name='Record_descriptor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=0)),
                ('draft_level', models.IntegerField(default=0)),
                ('feedback_level', models.IntegerField(default=0)),
                ('final_level', models.IntegerField(default=0)),
                ('draft_statement', models.TextField()),
                ('feedback_statement', models.TextField()),
                ('final_statement', models.TextField()),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chemtrack_app.Record_category')),
                ('record_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chemtrack_app.Record')),
                ('template_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chemtrack_app.Descriptor_template')),
            ],
        ),
    ]
