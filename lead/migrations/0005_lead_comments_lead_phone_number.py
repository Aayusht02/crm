# Generated by Django 5.1.3 on 2024-12-16 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0004_lead_lead_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='comments',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='lead',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
