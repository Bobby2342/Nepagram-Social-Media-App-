# Generated by Django 4.2.4 on 2023-08-20 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_conversation_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='conversation',
        ),
        migrations.RemoveField(
            model_name='message',
            name='sender',
        ),
        migrations.DeleteModel(
            name='Conversation',
        ),
        migrations.DeleteModel(
            name='Message',
        ),
    ]