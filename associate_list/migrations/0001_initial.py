# Generated by Django 5.1.3 on 2024-12-16 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Associate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=255)),
                ('company_type', models.CharField(max_length=100)),
                ('contact_person', models.CharField(max_length=255)),
                ('specialization', models.CharField(max_length=255)),
                ('skills', models.TextField()),
                ('phone_number', models.CharField(max_length=20)),
                ('comments', models.TextField(blank=True, null=True)),
            ],
        ),
    ]