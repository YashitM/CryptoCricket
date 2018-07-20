from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404

from website.models import Profile, Card
from .forms import RegisterForm, LoginForm

text_s = ["Player", "Owner", "Tournament", "Board", "Country", "ICC"]
text_p = ["Players", "Owners", "Tournaments", "Boards", "Countries", "ICCs"]


def home(request):
    all_players = Card.objects.all().filter(card_type=text_s[0])
    all_owners = Card.objects.all().filter(card_type=text_s[1])
    all_tournaments = Card.objects.all().filter(card_type=text_s[2])
    all_boards = Card.objects.all().filter(card_type=text_s[3])
    all_countries = Card.objects.all().filter(card_type=text_s[4])
    all_iccs = Card.objects.all().filter(card_type=text_s[5])

    context = {
        "players": all_players,
        "owners": all_owners,
        "tournaments": all_tournaments,
        "boards": all_boards,
        "countries": all_countries,
        "iccs": all_iccs,
        "categories": text_p,
    }

    return render(request, 'website/index.html', context)


def register(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = RegisterForm(request.POST)
            if form.is_valid():
                user = form.save()
                user.refresh_from_db()

                first_name = form.cleaned_data['first_name']
                last_name = form.cleaned_data['last_name']
                username = form.cleaned_data['username']
                email = form.cleaned_data['email']
                eth_address = form.cleaned_data['eth_address']
                password = form.cleaned_data['password']
                confirm_password = form.cleaned_data['confirm_password']
                if password == confirm_password:
                    profile, created = Profile.objects.get_or_create(user=user)
                    profile.eth_address = eth_address
                    profile.save()
                    user.user_profile = profile
                    user.save()
                    login(request, user)

                    return redirect('home')
        else:
            form = RegisterForm

        return render(request, 'website/register.html', {"form": form})
    else:
        return render(request, 'website/index.html', context=None)


def login_user(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request.POST)
            if form.is_valid():

                username = form.cleaned_data['username']
                password = form.cleaned_data['password']

                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('home')
        else:
            form = LoginForm

        return render(request, 'website/login.html', {"form": form})
    else:
        return render(request, 'website/index.html', context=None)


def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
    return render(request, 'website/index.html', context=None)


# MARKETPLACE


def marketplace_players(request):
    all_players = Card.objects.all().filter(card_type=text_s[0])
    return render(request, 'website/marketplace.html', {'items': all_players, 'text_s': text_s[0], 'text_p': text_p[0]})


def marketplace_team_owners(request):
    all_owners = Card.objects.all().filter(card_type=text_s[1])
    return render(request, 'website/marketplace.html', {'items': all_owners, 'text_s': text_s[1], 'text_p': text_p[1]})


def marketplace_tournaments(request):
    all_tournaments = Card.objects.all().filter(card_type=text_s[2])
    return render(request, 'website/marketplace.html',
                  {'items': all_tournaments, 'text_s': text_s[2], 'text_p': text_p[2]})


def marketplace_boards(request):
    all_boards = Card.objects.all().filter(card_type=text_s[3])
    return render(request, 'website/marketplace.html', {'items': all_boards, 'text_s': text_s[3], 'text_p': text_p[3]})


def marketplace_countries(request):
    all_countries = Card.objects.all().filter(card_type=text_s[4])
    return render(request, 'website/marketplace.html',
                  {'items': all_countries, 'text_s': text_s[4], 'text_p': text_p[4]})


def marketplace_iccs(request):
    all_iccs = Card.objects.all().filter(card_type=text_s[5])
    return render(request, 'website/marketplace.html', {'items': all_iccs, 'text_s': text_s[5], 'text_p': text_p[5]})


# CARD DETAILS

def card_details(request, item_id):
    selected_item = get_object_or_404(Card, pk=item_id)
    card_type = selected_item.card_type
    index = text_s.index(card_type)
    return render(request, 'website/details.html',
                  {'item': selected_item, 'text_s': text_s[index], 'text_p': text_p[index]})


def successful_transaction(request, item_id, current_bid, item_type):
    global selected_item
    current_user = request.user

    if item_type == "Player":
        selected_item = get_object_or_404(Player, pk=item_id)
    else:
        selected_item = get_object_or_404(Card, pk=item_id)

    selected_item.last_bid = current_bid
    selected_item.owner = current_user
    selected_item.save()
