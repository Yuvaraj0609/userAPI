import json
from django.core.management.base import BaseCommand
from users.models import User
import requests

class Command(BaseCommand):
    help = 'Load users from external JSON'

    def handle(self, *args, **kwargs):
        url = 'https://datapeace-storage.s3-us-west-2.amazonaws.com/dummy_data/users.json'
        response = requests.get(url)
        data = response.json()
        for item in data:
            User.objects.update_or_create(
                id=item['id'],
                defaults={
                    'first_name': item['first_name'],
                    'last_name': item['last_name'],
                    'company_name': item['company_name'],
                    'city': item['city'],
                    'state': item['state'],
                    'zip': item['zip'],
                    'email': item['email'],
                    'web': item['web'],
                    'age': item['age']
                }
            )
        self.stdout.write(self.style.SUCCESS('Users loaded successfully.'))