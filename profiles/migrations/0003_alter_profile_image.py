# Generated by Django 3.2.23 on 2023-12-02 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20231125_0743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='../default_profile_pz46wh', upload_to='images/'),
        ),
    ]
