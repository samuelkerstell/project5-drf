# Generated by Django 3.2.23 on 2023-12-02 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='../default_post_tx9uwa.jpg', upload_to='images/'),
        ),
    ]
