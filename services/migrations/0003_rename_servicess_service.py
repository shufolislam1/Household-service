# Generated by Django 4.2.7 on 2024-03-12 19:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_rename_services_servicess'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Servicess',
            new_name='Service',
        ),
    ]
