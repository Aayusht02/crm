# Generated by Django 5.1.3 on 2024-11-26 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0003_lead_resume'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='lead_type',
            field=models.CharField(choices=[('company', 'Company'), ('contact person', 'Contact Person')], default='company', max_length=20),
        ),
    ]
