# Generated by Django 4.2.12 on 2024-12-02 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tags', '0007_post_tag_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hub_tag',
            name='tagged_hubs',
        ),
        migrations.AlterField(
            model_name='post_tag',
            name='color',
            field=models.CharField(blank=True, default='#cfbc0d', max_length=20),
        ),
    ]
