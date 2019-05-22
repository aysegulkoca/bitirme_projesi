from django.db import models


class Scanweb(models.Model):
    url = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    sqlInjection =  models.CharField(max_length=200)
    xss = models.CharField(max_length=200)

    def __str__(self):
        return self.title
