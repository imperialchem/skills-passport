from django.db import models


class Assignment(models.Model):
    student_cid = models.CharField(max_length=15)
    teacher_cid = models.CharField(max_length=15)


class Category_template(models.Model):
    name = models.CharField(max_length=200, default="")
    description = models.TextField(default="")

    def __str__(self):
        return f"{self.pk} : {self.name}"


class Descriptor_template(models.Model):
    name = models.CharField(max_length=200, default="")
    description = models.TextField(default="")

    def __str__(self):
        return f"{self.pk} : {self.name}"


class Record(models.Model):
    date_creation = models.DateTimeField(auto_now_add=True)
    student_cid = models.CharField(max_length=15)
    date = models.DateTimeField()
    state = models.IntegerField(default=0)
    levels = models.CharField(max_length=200)
    name = models.CharField(max_length=100, default="")
    description = models.TextField(default="")


class Record_category(models.Model):
    template_id = models.ForeignKey(Category_template, on_delete=models.CASCADE)
    record_id = models.ForeignKey(Record, on_delete=models.CASCADE)
    level = models.IntegerField(default=0)


class Record_descriptor(models.Model):
    template_id = models.ForeignKey(Descriptor_template, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Record_category, on_delete=models.CASCADE)
    draft_level = models.IntegerField(default=0)
    feedback_level = models.IntegerField(default=0)
    final_level = models.IntegerField(default=0)
    draft_statement = models.TextField(default="")
    feedback_statement = models.TextField(default="")
    final_statement = models.TextField(default="")
