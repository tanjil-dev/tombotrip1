# Generated by Django 3.1.6 on 2021-04-25 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0036_auto_20210425_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='traveller',
            field=models.IntegerField(default=0),
        ),
    ]