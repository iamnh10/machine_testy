# Generated by Django 4.1.7 on 2023-03-25 14:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='contact_info',
            new_name='client_name',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='name',
            new_name='created_by',
        ),
        migrations.RemoveField(
            model_name='client',
            name='address',
        ),
        migrations.AddField(
            model_name='client',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
