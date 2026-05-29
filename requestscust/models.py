from django.db import models

class CustomerRequest(models.Model):
    Choices= [
        ('queued','QUEUED'),
        ('in_progress','IN PROGRESS'),
        ('resolved','RESOLVED'),
    ]
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    message = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=Choices,
        default='queued'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer_name} - {self.status}"
