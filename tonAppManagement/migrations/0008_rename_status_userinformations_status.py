# Generated by Django 4.2.5 on 2023-09-26 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tonAppManagement', '0007_rename_status_userinformations_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinformations',
            old_name='Status',
            new_name='status',
        ),
    ]
