# Generated by Django 4.2.1 on 2023-08-18 23:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_message'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Message',
        ),
    ]