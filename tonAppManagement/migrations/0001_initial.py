# Generated by Django 4.2.5 on 2023-09-24 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserInformations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('secondname', models.CharField(max_length=40)),
                ('service', models.CharField(max_length=50)),
                ('number', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
