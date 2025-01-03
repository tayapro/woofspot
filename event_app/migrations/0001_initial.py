# Generated by Django 5.1.3 on 2024-11-12 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WoofspotEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('content', models.TextField()),
                ('location', models.CharField(max_length=200)),
                ('event_date', models.DateField()),
                ('event_start_time', models.TimeField()),
                ('event_end_time', models.TimeField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Pet-Friendly Event',
                'ordering': ['-event_date', 'event_start_time'],
            },
        ),
    ]
