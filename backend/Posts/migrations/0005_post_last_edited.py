# Generated by Django 4.2.15 on 2024-11-17 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0004_remove_post_dislikes_alter_post_hub_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='last_edited',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
