# Generated by Django 4.2.15 on 2024-11-22 14:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hubs', '0003_hub_pending_members'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Events', '0012_alter_event_author_alter_event_hub'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_events', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='event',
            name='hub',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hub_events', to='hubs.hub'),
        ),
    ]
