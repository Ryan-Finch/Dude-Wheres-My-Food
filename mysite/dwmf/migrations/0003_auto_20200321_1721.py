# Generated by Django 3.0.4 on 2020-03-22 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dwmf', '0002_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='is_owner',
        ),
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='truck_owner',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
