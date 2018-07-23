from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db import models


class Card(models.Model):

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

    name = models.CharField(max_length=100, null=False)
    description = models.TextField(max_length=3000)
    transactions = models.IntegerField(default=0, null=False)
    owner = models.CharField(max_length=50, default="Unassigned")
    last_bid = models.CharField(default="0", max_length=30)
    eth_id = models.IntegerField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    icc_ranking = models.IntegerField(blank=True, null=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    ipl_team = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.card_type + ": " + self.name


class Profile(models.Model):
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE, related_name='user_profile')
    eth_address = models.CharField(max_length=43, null=False, blank=False)
    transactions = models.IntegerField(default=0, null=False)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name
