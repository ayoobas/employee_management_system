# Generated by Django 5.0 on 2024-01-06 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='rollnumber',
            new_name='employeeid',
        ),
    ]
