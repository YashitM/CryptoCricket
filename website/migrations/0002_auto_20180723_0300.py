# Generated by Django 2.0 on 2018-07-22 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='last_bid',
            field=models.CharField(default='0', max_length=30),
        ),
    ]
