# Generated by Django 3.1.6 on 2021-04-19 07:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0027_chatmessage_message_thread'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thread',
            name='first',
        ),
        migrations.RemoveField(
            model_name='thread',
            name='second',
        ),
        migrations.DeleteModel(
            name='ChatMessage',
        ),
        migrations.DeleteModel(
            name='Thread',
        ),
    ]
