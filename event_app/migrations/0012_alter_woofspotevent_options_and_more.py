# Generated by Django 5.1.3 on 2025-01-15 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event_app', '0011_alter_woofspotevent_event_date_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='woofspotevent',
            options={'ordering': ['-date', 'start_time'], 'verbose_name': 'The Event'},
        ),
        migrations.RenameField(
            model_name='woofspotevent',
            old_name='event_date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='woofspotevent',
            old_name='content',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='woofspotevent',
            old_name='event_end_time',
            new_name='end_time',
        ),
        migrations.RenameField(
            model_name='woofspotevent',
            old_name='event_start_time',
            new_name='start_time',
        ),
    ]
