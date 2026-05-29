from django.db import models
from requestscust.models import CustomerRequest

class Classification(models.Model):
    Choices= [
        ('support','SUPPROT'),
        ('sales','SALES'),
        ('billing','BILLING'),
    ]

    Priority_Choices = [
        ('low','LOW'),
        ('medium','MEDIUM'),
        ('high','HIGH'),
    ]

    request = models.OneToOneField(
        CustomerRequest,
        on_delete=models.CASCADE
    )
    category = models.CharField(
        max_length=20,
        choices=Choices
    )
    priority = models.CharField(
        max_length=20,
        choices=Priority_Choices
    )
    
    def __str__(self):
        return f"{self.request.id} - {self.category}"

