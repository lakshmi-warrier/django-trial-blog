# Generated by Django 3.1.7 on 2023-05-19 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0005_auto_20230519_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default='2020-01-01 00:00:00.000000'),
        ),
    ]