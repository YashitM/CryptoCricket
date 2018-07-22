from .forms import BuyForm
from django.conf import settings

marketplace_item_list = ['Players', 'ICC', 'Countries', 'Boards', 'Tournaments', 'Team Owners']


def marketplace_items_context(request):
    return {
        'marketplace_items': marketplace_item_list,
        'multiplier_0': settings.MULTIPLIER_0,
        'multiplier_1': settings.MULTIPLIER_1,
        'multiplier_2': settings.MULTIPLIER_2,
        'multiplier_default': settings.MULTIPLIER_DEFAULT,
        'buy_form': BuyForm,
    }
