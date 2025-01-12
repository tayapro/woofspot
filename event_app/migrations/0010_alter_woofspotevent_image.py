# Generated by Django 5.1.3 on 2025-01-12 20:47

import cloudinary.models
import event_app.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event_app', '0009_alter_rating_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='woofspotevent',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, validators=[event_app.models.file_validation], verbose_name='image'),
        ),
    ]
