from django import template
from django.conf import settings
from ..models import Card

register = template.Library()


@register.filter
def multiply(qty, unit_price):
    prod = float(qty) * float(unit_price)
    comm = (1 + settings.COMMISSION / 100) * prod
    return comm


@register.filter
def check_category(category):
    items = Card.objects.all()
    for item in items:
        if item.card_type == category:
            return True
    return False
