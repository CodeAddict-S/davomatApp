# Generated by Django 5.1.5 on 2025-02-03 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fingerprints', '0006_attendances'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Attendances',
            new_name='Attendance',
        ),
    ]
