from django.db import models

# Create your models here.

class MenuItem(models.Model):
    title = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    url = models.CharField(max_length=200, blank=True)
    named_url = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title
