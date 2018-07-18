from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

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
    text_singular = "ICC"
    text_plural = "ICC"
    return render(request, 'website/marketplace/common.html',
                  {'items': all_iccs, 'text_s': text_singular, 'text_p': text_plural})


def marketplace_countries(request):
    all_countries = Country.objects.all()
    text_singular = "Country"
    text_plural = "Countries"
    return render(request, 'website/marketplace/common.html',
                  {'items': all_countries, 'text_s': text_singular, 'text_p': text_plural})


def marketplace_players(request):
    all_players = Player.objects.all()
    text_singular = "Player"
    text_plural = "Players"
    return render(request, 'website/marketplace/common.html',
                  {'items': all_players, 'text_s': text_singular, 'text_p': text_plural})


def marketplace_tournaments(request):
    all_tournaments = Tournament.objects.all()
    text_singular = "Tournament"
    text_plural = "Tournaments"
    return render(request, 'website/marketplace/common.html',
                  {'items': all_tournaments, 'text_s': text_singular, 'text_p': text_plural})


def marketplace_boards(request):
    all_boards = CricketBoard.objects.all()
    text_singular = "Board"
    text_plural = "Boards"
    return render(request, 'website/marketplace/common.html',
                  {'items': all_boards, 'text_s': text_singular, 'text_p': text_plural})


def marketplace_team_owners(request):
    all_owners = TeamOwner.objects.all()
    text_singular = "Team Owner"
    text_plural = "Team Owners"
    return render(request, 'website/marketplace/common.html', {'items': all_owners, 'text_s': text_singular, 'text_p': text_plural})
