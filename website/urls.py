from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home, name='home'),

    # Authentication URLs

    path('register', views.register, name='register'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),

    # Marketplace URLs

    path('players', views.marketplace_players, name='players'),
    path('iccs', views.marketplace_iccs, name='iccs'),
    path('countries', views.marketplace_countries, name='countries'),
    path('tournaments', views.marketplace_tournaments, name='tournaments'),
    path('boards', views.marketplace_boards, name='boards'),
    path('owners', views.marketplace_team_owners, name='owners'),

    # Details URLs

    path('players/<int:item_id>', views.player_details, name='player'),
    path('countries/<int:item_id>', views.card_details, name='country'),
    path('owners/<int:item_id>', views.card_details, name='owner'),
    path('boards/<int:item_id>', views.card_details, name='board'),
    path('iccs/<int:item_id>', views.card_details, name='icc'),
    path('tournaments/<int:item_id>', views.card_details, name='tournament'),


]