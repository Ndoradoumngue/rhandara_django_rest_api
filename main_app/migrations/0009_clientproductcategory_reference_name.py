# Generated by Django 3.1.13 on 2021-08-09 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_userwhatsappmessage_response'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientproductcategory',
            name='reference_name',
            field=models.CharField(default='men-clothing', max_length=50),
            preserve_default=False,
        ),
    ]
