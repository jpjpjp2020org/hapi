# core/models.py

from django.db import models

# data that answers what and how much, where and when
class SMSData(models.Model):
    phone_number = models.CharField(max_length=25)
    message_content = models.TextField()
    resource_needed = models.CharField(max_length=200, blank=True, null=True)
    quantity = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    timeline = models.CharField(max_length=200, blank=True, null=True)
    evaluation = models.CharField(max_length=20, choices=[('incomplete', 'Incomplete'), ('complete', 'Complete')], default='incomplete')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.phone_number}: {self.message_content[:50]}..."



# incomplete data for collation and aggregation and oversight of not missing requests
class SMSValDump(models.Model):
    phone_number = models.CharField(max_length=25)
    message_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Raw SMS from {self.phone_number}: {self.message_content[:50]}..."
