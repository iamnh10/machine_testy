# Generated by Django 4.1.7 on 2023-03-26 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_alter_client_created_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='description',
        ),
        migrations.RemoveField(
            model_name='project',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='project',
            name='start_date',
        ),
    ]
