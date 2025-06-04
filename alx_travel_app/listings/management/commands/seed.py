import random
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from listings.models import Listing

User = get_user_model()

class Command(BaseCommand):
    help = "Seed the database with sample listings"

    def handle(self, *args, **kwargs):
        user, created = User.objects.get_or_create(
            username='owner',
            defaults={'email': 'owner@example.com'}
        )

        if created:
            user.set_password('password123')
            user.save()

        sample_listings = [
            {
                "title": "Cozy Cottage",
                "description": "A lovely small cottage in the countryside.",
                "price_per_night": 50,
                "location": "Countryside"
            },
            {
                "title": "Beachfront Bungalow",
                "description": "Beautiful bungalow with sea views.",
                "price_per_night": 120,
                "location": "Beach"
            },
            {
                "title": "City Apartment",
                "description": "Modern apartment in the heart of the city.",
                "price_per_night": 85,
                "location": "City Center"
            },
        ]

        for data in sample_listings:
            listing, created = Listing.objects.get_or_create(
                title=data['title'],
                defaults={
                    'description': data['description'],
                    'price_per_night': data['price_per_night'],
                    'location': data['location'],
                    'owner': user,
                }
            )
            if created:
                self.stdout.write(f'✅ Created listing: {listing.title}')
            else:
                self.stdout.write(f'ℹ️ Listing already exists: {listing.title}')
