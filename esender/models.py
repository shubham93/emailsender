from django.db import models

# Create your models here.

class email_data(models.Model):
    subject=models.TextField()
    message=models.TextField()
    email=models.TextField()
