# Generated by Django 3.1.13 on 2021-08-07 10:46

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_userwhatsappmessage'),
    ]

    operations = [
        migrations.AddField(
            model_name='userwhatsappmessage',
            name='response',
            field=ckeditor.fields.RichTextField(default=1),
            preserve_default=False,
        ),
    ]
