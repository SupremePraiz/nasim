# Generated by Django 4.1.7 on 2023-06-27 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_alter_profile_date_of_birth_alter_profile_gender_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='User',
            new_name='user',
        ),
    ]