from django import template

register = template.Library()


@register.filter
def multiply(qty, unit_price):
    return float(qty) * float(unit_price)
