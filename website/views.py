from django.contrib.auth import authenticate, login, logout
from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required

from website.models import Profile, Card
from .forms import RegisterForm, BuyForm

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
        "players": all_players[:5],
        "owners": all_owners[:5],
        "tournaments": all_tournaments[:5],
        "boards": all_boards[:5],
        "countries": all_countries[:5],
        "iccs": all_iccs[:5],
        "categories": text_p[:5],
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
                    profile = Profile()
                    profile.user_id = user.id
                    profile.eth_address = eth_address
                    profile.save()
                    user.set_password(password)
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

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')

        return render(request, 'website/login.html', context=None)
    else:
        return render(request, 'website/index.html', context=None)


def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
    return render(request, 'website/index.html', context=None)


# MARKETPLACE


def marketplace_players(request):
    all_players = Card.objects.all().filter(card_type=text_s[0])
    context = {'items': all_players, 'text_s': text_s[0], 'text_p': text_p[0]}
    if not request.user.is_staff and request.user.is_authenticated:
        profile = get_object_or_404(Profile, user_id=request.user.id)
        context['eth_address'] = profile.eth_address
    return render(request, 'website/marketplace.html', context=context)


def marketplace_team_owners(request):
    all_owners = Card.objects.all().filter(card_type=text_s[1])
    context = {'items': all_owners, 'text_s': text_s[1], 'text_p': text_p[1]}
    if not request.user.is_staff and request.user.is_authenticated:
        profile = get_object_or_404(Profile, user_id=request.user.id)
        context['eth_address'] = profile.eth_address
    return render(request, 'website/marketplace.html', context=context)


def marketplace_tournaments(request):
    all_tournaments = Card.objects.all().filter(card_type=text_s[2])
    context = {'items': all_tournaments, 'text_s': text_s[2], 'text_p': text_p[2]}
    if not request.user.is_staff and request.user.is_authenticated:
        profile = get_object_or_404(Profile, user_id=request.user.id)
        context['eth_address'] = profile.eth_address
    return render(request, 'website/marketplace.html', context=context)


def marketplace_boards(request):
    all_boards = Card.objects.all().filter(card_type=text_s[3])
    context = {'items': all_boards, 'text_s': text_s[3], 'text_p': text_p[3]}
    if not request.user.is_staff and request.user.is_authenticated:
        profile = get_object_or_404(Profile, user_id=request.user.id)
        context['eth_address'] = profile.eth_address
    return render(request, 'website/marketplace.html', context=context)


def marketplace_countries(request):
    all_countries = Card.objects.all().filter(card_type=text_s[4])
    context = {'items': all_countries, 'text_s': text_s[4], 'text_p': text_p[4]}
    if not request.user.is_staff and request.user.is_authenticated:
        profile = get_object_or_404(Profile, user_id=request.user.id)
        context['eth_address'] = profile.eth_address
    return render(request, 'website/marketplace.html', context=context)


def marketplace_iccs(request):
    all_iccs = Card.objects.all().filter(card_type=text_s[5])
    context = {'items': all_iccs, 'text_s': text_s[5], 'text_p': text_p[5]}
    if not request.user.is_staff and request.user.is_authenticated:
        profile = get_object_or_404(Profile, user_id=request.user.id)
        context['eth_address'] = profile.eth_address
    return render(request, 'website/marketplace.html', context=context)


# CARD DETAILS

def card_details(request, item_id):
    selected_item = get_object_or_404(Card, pk=item_id)
    card_type = selected_item.card_type
    index = text_s.index(card_type)
    context = {'item': selected_item, 'text_s': text_s[index], 'text_p': text_p[index]}
    if not request.user.is_staff and request.user.is_authenticated:
        profile = get_object_or_404(Profile, user_id=request.user.id)
        context['eth_address'] = profile.eth_address
    return render(request, 'website/details.html', context=context)


# @login_required
def successful_transaction(request):
    if request.method == "POST":
        current_user = request.user
        form = BuyForm(request.POST)
        if form.is_valid():
            item_id = form.cleaned_data['item_id']
            current_bid = form.cleaned_data['updated_price']
            selected_item = get_object_or_404(Card, eth_id=item_id)
            selected_item.transactions = selected_item.transactions + 1
            selected_item.last_bid = current_bid
            selected_item.owner = current_user.user_profile.eth_address
            selected_item.save()
        else:
            print(form.errors)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
