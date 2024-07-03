# myapp/models.py
from django.db import models

class Employee(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='employee_images/', null=True, blank=True)  # new field

    def __str__(self):
        return f"{self.code} - {self.name}"
