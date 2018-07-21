# Generated by Django 2.0 on 2018-07-21 15:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_type', models.CharField(choices=[('Player', 'Player'), ('Owner', 'Owner'), ('Tournament', 'Tournament'), ('Board', 'Board'), ('Country', 'Country'), ('ICC', 'ICC')], default='Player', max_length=11)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=3000)),
                ('owner', models.CharField(default='Unassigned', max_length=50)),
                ('last_bid', models.FloatField(default=0)),
                ('eth_id', models.IntegerField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('icc_ranking', models.IntegerField(blank=True, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('ipl_team', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eth_address', models.CharField(max_length=43)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
