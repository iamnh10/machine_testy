# Generated by Django 4.1.7 on 2023-03-25 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_contact_info_client_client_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='created_by',
        ),
    ]
