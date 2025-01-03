# Generated by Django 5.1.3 on 2024-12-20 07:55

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('time_tracker', '0003_remove_attendance_overtime_hours_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendance',
            old_name='employee',
            new_name='user',
        ),
        migrations.AlterUniqueTogether(
            name='attendance',
            unique_together={('user', 'date')},
        ),
    ]
