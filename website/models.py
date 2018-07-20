from django.contrib.auth.models import User
from django.db import models


class Card(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.TextField(max_length=3000)
    transactions = 0
    owner = models.ForeignKey(User, models.SET_NULL, blank=True, null=True)
    last_bid = models.FloatField(default=0)
    eth_id = models.IntegerField(null=True, blank=True)

    CARD_TYPES = (
        ("Player", 'Player'),
        ("Owner", 'Owner'),
        ("Tournament", 'Tournament'),
        ("Board", 'Board'),
        ("Country", 'Country'),
        ("ICC", 'ICC'),

    )

    card_type = models.CharField(
        max_length=11,
        choices=CARD_TYPES,
        default="Player"
    )

    def __str__(self):
        return self.card_type + ": " + self.name


class Player(Card):
    icc_ranking = models.IntegerField()
    country = models.CharField(max_length=100, null=False)
    ipl_team = models.CharField(max_length=100, null=True)
    image = models.ImageField(null=True, blank=True)


class Profile(models.Model):
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE, related_name='user_profile')
    eth_address = models.CharField(max_length=30, null=False, blank=False)
    last_bid = models.FloatField()
    transactions = 0