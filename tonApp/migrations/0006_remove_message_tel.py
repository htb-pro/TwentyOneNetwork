# Generated by Django 4.2.3 on 2023-08-14 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tonApp', '0005_alter_message_tel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='Tel',
        ),
    ]
