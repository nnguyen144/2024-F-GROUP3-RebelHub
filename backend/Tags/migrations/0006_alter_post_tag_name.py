# Generated by Django 4.2.12 on 2024-11-29 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tags', '0005_delete_tag_post_tag_hub_hub_tag_tagged_hubs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post_tag',
            name='name',
            field=models.CharField(max_length=16),
        ),
    ]
