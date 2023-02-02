from django.db import models
from . import constants as task_constants

class Todo(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField(blank=True, default='')
    status = models.PositiveSmallIntegerField(choices=task_constants.TASK_TYPE_CHOICES, default=task_constants.OPEN)

    class Meta:
        ordering = ['created_at']
        db_table = "todos"
