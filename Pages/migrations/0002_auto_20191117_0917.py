# Generated by Django 2.2.7 on 2019-11-17 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='profile_pic',
            field=models.ImageField(upload_to='about', verbose_name='Profilkép'),
        ),
    ]
