from django.db import models

# Create your models here.

class Job(models.Model):
    image=models.ImageField(upload_to='images')
    title=models.TextField(default='Measure of Zone of Inhibation')
    summary=models.TextField()

    def __str__(self):
        return self.title