from django.db import models

# Create your models here.


class Report(models.Model):
    ip = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
