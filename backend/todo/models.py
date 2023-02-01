from django.db import models

class Todo(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField(blank=True, default='')
    status = models.CharField(max_length=20, default='open') #open, doing, done, pending

    class Meta:
        ordering = ['created']
