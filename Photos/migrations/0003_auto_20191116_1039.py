# Generated by Django 2.2.7 on 2019-11-16 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Photos', '0002_auto_20191116_1023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Név'),
        ),
    ]
