from django.db import models


class Assignment(models.Model):
    student_cid = models.CharField(max_length=15)
    teacher_cid = models.CharField(max_length=15)


class Category_template(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name


class Descriptor_template(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    category_id = models.ForeignKey(Category_template, on_delete=models.CASCADE)


    def __str__(self):
        return self.name


class Record(models.Model):
    date_creation = models.DateTimeField(auto_now_add=True)
    student_cid = models.CharField(max_length=15)
    state = models.IntegerField(default=0)
    levels = models.CharField(max_length=200)


class Record_category(models.Model):
    template_id = models.ForeignKey(Category_template, on_delete=models.CASCADE)
    record_id = models.ForeignKey(Record, on_delete=models.CASCADE)
    level = models.IntegerField(default=0)
    order = models.IntegerField(default=0)


class Record_descriptor(models.Model):
    template_id = models.ForeignKey(Descriptor_template, on_delete=models.CASCADE)
    record_id = models.ForeignKey(Record, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Record_category, on_delete=models.CASCADE)
    order = models.IntegerField(default=0)
    draft_level = models.IntegerField(default=0)
    feedback_level = models.IntegerField(default=0)
    final_level = models.IntegerField(default=0)
    draft_statement = models.TextField()
    feedback_statement = models.TextField()
    final_statement = models.TextField()
    order = models.IntegerField(default=0)
