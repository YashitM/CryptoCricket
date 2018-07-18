from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404

from website.models import Profile, Player, ICC, Country, Tournament, CricketBoard, TeamOwner
from .forms import RegisterForm, LoginForm


def home(request):
    return render(request, 'website/index.html', context=None)


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


def marketplace_iccs(request):
    all_iccs = ICC.objects.all()
    text_s = "ICC"
    text_p = "ICC"
    return render(request, 'website/marketplace.html', {'items': all_iccs, 'text_s': text_s, 'text_p': text_p})


def marketplace_countries(request):
    all_countries = Country.objects.all()
    text_s = "Country"
    text_p = "Countries"
    return render(request, 'website/marketplace.html', {'items': all_countries, 'text_s': text_s, 'text_p': text_p})


def marketplace_players(request):
    all_players = Player.objects.all()
    text_s = "Player"
    text_p = "Players"
    return render(request, 'website/marketplace.html', {'items': all_players, 'text_s': text_s, 'text_p': text_p})


def marketplace_tournaments(request):
    all_tournaments = Tournament.objects.all()
    text_s = "Tournament"
    text_p = "Tournaments"
    return render(request, 'website/marketplace.html', {'items': all_tournaments, 'text_s': text_s, 'text_p': text_p})


def marketplace_boards(request):
    all_boards = CricketBoard.objects.all()
    text_s = "Board"
    text_p = "Boards"
    return render(request, 'website/marketplace.html', {'items': all_boards, 'text_s': text_s, 'text_p': text_p})


def marketplace_team_owners(request):
    all_owners = TeamOwner.objects.all()
    text_s = "Owner"
    text_p = "Owners"
    return render(request, 'website/marketplace.html', {'items': all_owners, 'text_s': text_s, 'text_p': text_p})


def player_details(request, item_id):
    selected_item = get_object_or_404(Player, pk=item_id)
    text_s = "Player"
    text_p = "Players"
    return render(request, 'website/details.html', {'item': selected_item, 'text_s': text_s, 'text_p': text_p})


def country_details(request, item_id):
    selected_item = get_object_or_404(Country, pk=item_id)
    text_s = "Country"
    text_p = "Countries"
    return render(request, 'website/details.html', {'item': selected_item, 'text_s': text_s, 'text_p': text_p})


def owner_details(request, item_id):
    selected_item = get_object_or_404(TeamOwner, pk=item_id)
    text_s = "Owner"
    text_p = "Owners"
    return render(request, 'website/details.html', {'item': selected_item, 'text_s': text_s, 'text_p': text_p})


def board_details(request, item_id):
    selected_item = get_object_or_404(CricketBoard, pk=item_id)
    text_s = "Board"
    text_p = "Boards"
    return render(request, 'website/details.html', {'item': selected_item, 'text_s': text_s, 'text_p': text_p})


def icc_details(request, item_id):
    selected_item = get_object_or_404(ICC, pk=item_id)
    text_s = "Board"
    text_p = "Boards"
    return render(request, 'website/details.html', {'item': selected_item, 'text_s': text_s, 'text_p': text_p})


def tournament_details(request, item_id):
    selected_item = get_object_or_404(Tournament, pk=item_id)
    text_s = "Board"
    text_p = "Boards"
    return render(request, 'website/details.html', {'item': selected_item, 'text_s': text_s, 'text_p': text_p})


def successful_transaction(request, item_id, current_bid, item_type):
    global selected_item
    current_user = request.user

    if item_type == "Player":
        selected_item = Player.objects.get(pk=item_id)
    elif item_type == "Board":
        selected_item = CricketBoard.objects.get(pk=item_id)
    elif item_type == "Country":
        selected_item = Country.objects.get(pk=item_id)
    elif item_type == "Owner":
        selected_item = TeamOwner.objects.get(pk=item_id)
    elif item_type == "Tournament":
        selected_item = Tournament.objects.get(pk=item_id)
    elif item_type == "ICC":
        selected_item = ICC.objects.get(pk=item_id)

    selected_item.last_bid = current_bid
    selected_item.owner = current_user
    selected_item.save()


