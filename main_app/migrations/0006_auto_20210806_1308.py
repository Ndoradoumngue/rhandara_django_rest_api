# Generated by Django 3.1.13 on 2021-08-06 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_auto_20210806_0839'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companydetails',
            name='representation',
        ),
        migrations.RemoveField(
            model_name='companydetails',
            name='welcome_word',
        ),
    ]
