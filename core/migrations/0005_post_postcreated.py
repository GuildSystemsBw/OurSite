# Generated by Django 3.0.6 on 2020-06-07 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20200604_0108'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='postCreated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]