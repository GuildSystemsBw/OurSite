# Generated by Django 3.1.4 on 2021-05-23 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20210509_1535'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='visible',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='avi',
            field=models.ImageField(blank=True, null=True, upload_to='element/'),
        ),
    ]
