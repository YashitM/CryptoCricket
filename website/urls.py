from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('players', views.marketplace_players, name='players'),
    path('icc', views.marketplace_iccs, name='iccs'),
    path('countries', views.marketplace_countries, name='countries'),
    path('tournaments', views.marketplace_tournaments, name='tournaments'),
    path('boards', views.marketplace_boards, name='boards'),
    path('owners', views.marketplace_team_owners, name='owners'),
]