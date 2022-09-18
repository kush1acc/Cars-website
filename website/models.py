from django.db import models

# Create your models here.
class Contact(models.Model):
    name_1 = models.CharField(max_length=40)
    email = models.EmailField()
    subject = models.CharField(max_length=10)
    textarea = models.CharField(max_length=100)
    def __str__(self):
        return self.name_1



