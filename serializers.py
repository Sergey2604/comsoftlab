from rest_framework import serializers
from models.models import Email

class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = ['subject', 'sent_at', 'received_at', 'body', 'attachments']
