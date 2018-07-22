from django import template
from django.conf import settings

register = template.Library()


@register.filter
def multiply(qty, unit_price):
    prod = float(qty) * float(unit_price)
    comm = (1 + settings.COMMISSION / 100) * prod
    return comm
