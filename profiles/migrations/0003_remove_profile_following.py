# Generated by Django 3.0.5 on 2020-04-30 09:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20200430_1427'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='following',
        ),
    ]
