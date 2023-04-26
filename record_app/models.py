from django.db import models

# Create your models here.
class Employees(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    department = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}, {self.designation}, {self.department}"


class Files(models.Model):
    file_number = models.CharField(max_length=50)
    description = models.CharField(max_length=300, null=True, blank=True)
    
    def __str__(self):
        return f"{self.file_number}"


class Incoming(models.Model):
    document_number =models.IntegerField(unique=True)
    date_received =models.DateField(auto_now_add=False, auto_now=False)

    DOCUMENT_TYPE = [
        ('EM', 'Email'),
        ('LR', 'Letter'),
        ('OT', 'OTHER'),
    ]
    
    document_type = models.CharField(max_length=2,choices=DOCUMENT_TYPE)
    file_number = models.ForeignKey(Files, on_delete=models.CASCADE)
    received_from = models.CharField(max_length=100, null=True, blank=True)
    subject = models.CharField(max_length=300)
    description =models.TextField()
    marked_to = models.ForeignKey(Employees, null=True, on_delete=models.CASCADE, blank=True)

    STATUS = [
        ('FL', 'Filed'),
        ('IP', 'InProcess'),
    ]

    status = models.CharField(max_length=2,choices=STATUS, null=True, blank=True)
    url = models.URLField(null=True, default="https://www.google.com/", blank=True)

    def __str__(self):
        return f"ID: {self.document_number}, Subject: {self.subject}"

class Outgoing(models.Model):
    document_number = models.IntegerField(unique=True)
    date_dispatched = models.DateField(auto_now_add=False, auto_now=False)
    DOCUMENT_TYPE = [
        ('EM', 'Email'),
        ('LR', 'Letter'),
        ('OT', 'OTHER'),
    ]
    
    document_type = models.CharField(max_length=2,choices=DOCUMENT_TYPE)
    file_number = models.ForeignKey(Files, on_delete=models.CASCADE)
    sent_to = models.CharField(max_length=300, null=True, blank=True)
    subject = models.CharField(max_length=300)
    description = models.TextField()
    dispatched_by = models.ForeignKey(Employees, null=True, on_delete=models.CASCADE, blank=True)

    STATUS = [
        ('DP', 'Dispatched'),
        ('DL', 'Delivered'),
        ('RT', 'Returned'),
    ]
    status = models.CharField(max_length=2,choices=STATUS, blank=True)
    url = models.URLField(null=True, default="https://www.google.com/", blank=True)

    def __str__(self):
        return f"ID: {self.document_number}, Subject: {self.subject}"