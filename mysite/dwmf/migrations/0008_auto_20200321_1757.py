# Generated by Django 3.0.4 on 2020-03-22 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dwmf', '0007_auto_20200321_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='truck_owner',
            field=models.BooleanField(),
        ),
    ]
