# Generated by Django 4.2.7 on 2024-03-13 20:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_user_profile_picture'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='profile_Picture',
            new_name='profile_picture',
        ),
    ]
