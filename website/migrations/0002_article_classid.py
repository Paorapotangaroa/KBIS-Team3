# Generated by Django 4.1.3 on 2022-11-17 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='classID',
            field=models.CharField(default='IS403', max_length=5),
        ),
    ]
