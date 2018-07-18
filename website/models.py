from django.contrib.auth.models import User
from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=100, null=False)
    transactions = 0
    icc_ranking = models.IntegerField()
    country = models.CharField(max_length=100, null=False)
    ipl_team = models.CharField(max_length=100, null=True)
    last_bid = models.FloatField()
    image = models.ImageField(null=True, blank=True)
    description = models.TextField(max_length=3000)


class TeamOwner(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.TextField(max_length=3000)
    last_bid = models.FloatField(default=0)
    transactions = 0


class Tournament(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.TextField(max_length=3000)
    last_bid = models.FloatField()
    transactions = 0


class CricketBoard(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.TextField(max_length=3000)
    last_bid = models.FloatField()
    transactions = 0


class Country(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.TextField(max_length=3000)
    last_bid = models.FloatField()
    transactions = 0


class ICC(models.Model):
    board_name = models.CharField(max_length=100, null=False)
    description = models.TextField(max_length=3000)
    last_bid = models.FloatField()
    transactions = 0


class Profile(models.Model):
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE, related_name='user_profile')
    eth_address = models.CharField(max_length=30, null=False, blank=False)
    last_bid = models.FloatField()
    transactions = 0
