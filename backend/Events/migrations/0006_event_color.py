# Generated by Django 5.1.2 on 2024-10-22 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0005_alter_event_end_time_alter_event_start_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='color',
            field=models.CharField(blank=True, default='#eb4f34', max_length=20),
        ),
    ]