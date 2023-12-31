# Generated by Django 4.1.7 on 2023-06-27 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_delete_profilemodelform'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='date_of_birth',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('M', 'M'), ('F', 'F')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='local_government_area_of_origin',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='other_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(default='default.png', null=True, upload_to='pics'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='scheme_name',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='state_of_origin',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='year_of_application',
            field=models.DateField(null=True),
        ),
    ]
