# Generated by Django 3.1.6 on 2021-02-02 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='role',
            name='role',
        ),
        migrations.AlterField(
            model_name='role',
            name='name',
            field=models.CharField(max_length=40, unique=True),
        ),
    ]
