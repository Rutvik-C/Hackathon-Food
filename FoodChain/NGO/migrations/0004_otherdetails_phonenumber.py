# Generated by Django 3.0.8 on 2020-10-09 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NGO', '0003_auto_20201009_1633'),
    ]

    operations = [
        migrations.AddField(
            model_name='otherdetails',
            name='phonenumber',
            field=models.IntegerField(default=9898944),
        ),
    ]
