# Generated by Django 3.1.2 on 2021-02-27 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doner',
            name='id',
        ),
        migrations.RemoveField(
            model_name='reciever',
            name='id',
        ),
        migrations.AlterField(
            model_name='doner',
            name='phone_no',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='reciever',
            name='phone_no',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]
