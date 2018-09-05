from django.db import models


class TaskResult(models.Model):
    taskname = models.CharField(max_length=30)
    requested_user = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    created = models.DateField(auto_now_add=True)
