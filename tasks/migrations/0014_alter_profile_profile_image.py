# Generated by Django 5.0.7 on 2024-09-27 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0013_alter_profile_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, default='static/profile/default.jpg', null=True, upload_to='profile_images/'),
        ),
    ]
