from django.db import models

# Create your models here.
class Attendance (models.Model):
    id = models.IntegerField(primary_key=True)
    add = models.CharField(max_length=50, default="")
    user = models.CharField(max_length=50, default="")
    created_at = models.DateField(auto_now_add=True)
    clock_in = models.CharField(max_length=100, default=0)
    clock_out = models.TimeField(auto_now=True)
    # time = models.DateField()

    class Meta:
        db_table = "a"

    # forget link
# https://dev.to/earthcomfy/django-reset-password-3k0l

class Times(models.Model):
    id=models.IntegerField(primary_key=True)
    time=models.TimeField()

    class Meta:
        db_table="times"