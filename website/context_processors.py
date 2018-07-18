marketplace_item_list = ['Players', 'ICC', 'Countries', 'Boards', 'Tournaments', 'Team Owners']
multiplier = 1.2


def marketplace_items_context(request):
    return {
        'marketplace_items': marketplace_item_list,
        'multiplier': multiplier,
    }
