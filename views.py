from django.http import HttpResponse
from django.shortcuts import render
from models.models import Email
from serializers import EmailSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from github import Github
import requests

def login(request):
    # Implement login logic here
    return render(request, 'base.html')

def get_emails(request):
    # Retrieve emails from database and serialize them
    emails = Email.objects.all()
    serialized_emails = [EmailSerializer(email).data for email in emails]
    return render(request, 'emails.html', {'emails': serialized_emails})

class GmailLoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({'error': 'Username and password are required'}, status=400)

        try:
            gh = Github(username, password)
            # Verify the credentials
            gh.get_user().get('login')
            return Response({'message': 'Login successful'}, status=200)
        except Exception as e:
            return Response({'error': str(e)}, status=401)
