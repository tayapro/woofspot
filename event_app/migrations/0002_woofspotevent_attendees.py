# Generated by Django 5.1.3 on 2024-11-17 13:06

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='woofspotevent',
            name='attendees',
            field=models.ManyToManyField(blank=True, related_name='events_attending', to=settings.AUTH_USER_MODEL),
        ),
    ]