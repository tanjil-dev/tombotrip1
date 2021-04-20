# Generated by Django 3.1.6 on 2021-04-06 15:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_auto_20210406_1959'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserve',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(max_length=100)),
                ('employee_name', models.CharField(max_length=100)),
                ('cell_no', models.CharField(max_length=15)),
                ('address', models.TextField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('to', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.RemoveField(
            model_name='order',
            name='supply',
        ),
        migrations.AddField(
            model_name='order',
            name='first_name',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='last_name',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]