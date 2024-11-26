# Generated by Django 4.2.15 on 2024-11-26 03:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Private_Messaging', '0002_remove_conversation_messagecontent_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='conversation',
            old_name='conversationID',
            new_name='conversation_id',
        ),
        migrations.RenameField(
            model_name='conversation',
            old_name='creatorID',
            new_name='creator_id',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='conversationID',
            new_name='conversation_id',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='messageContent',
            new_name='message_content',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='messageID',
            new_name='message_id',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='messageTimestamp',
            new_name='message_timestamp',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='userID',
            new_name='user_id',
        ),
    ]
