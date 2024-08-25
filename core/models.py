from django.db import models

# Create your models here.
class SMSData(models.Model):
    phone_number = models.CharField(max_length=15)
    message_content = models.TextField()
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('complete', 'Complete')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.phone_number}: {self.message_content[:50]}..."