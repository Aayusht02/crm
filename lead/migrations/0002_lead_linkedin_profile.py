# Generated by Django 5.1.3 on 2024-11-21 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='linkedin_profile',
            field=models.URLField(blank=True, null=True),
        ),
    ]
