from django.db import models


class User(models.Model):
    username = models.CharField(max_length = 50)
    password = models.CharField(max_length = 255)


class Email(models.Model):
    subject = models.TextField()
    sent_at = models.DateTimeField()
    received_at = models.DateTimeField(null = True, blank = True)
    body = models.TextField()
    attachments = models.FileField(upload_to = 'attachments/')
