from django.db import models

class ServiceRequest(models.Model):
    REQUEST_TYPE_CHOICES = (
        ('LEAK', 'Leak Repair'),
        ('METER', 'Meter Reading/Replacement'),
        ('SERVICE', 'New Service/Disconnection'),
        ('OTHER', 'Other'),
    )
    customer_name = models.CharField(max_length=255)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=20)
    request_type = models.CharField(max_length=10, choices=REQUEST_TYPE_CHOICES)
    request_details = models.TextField()
    request_status = models.CharField(max_length=50, default='Pending')
    request_date = models.DateTimeField(auto_now_add=True)
    resolved_date = models.DateTimeField(null=True, blank=True)
    attached_file = models.FileField(upload_to='uploads/', blank=True)  #Optional file upload

class Account(models.Model):  
    customer = models.OneToOneField(ServiceRequest, on_delete=models.CASCADE)  #Link to ServiceRequest or other suitable model
    account_number = models.CharField(max_length=20)
