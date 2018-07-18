from django.contrib import admin
from .models import Country, CricketBoard, ICC, Player, TeamOwner, Tournament
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Profile


# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profile'


class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Country)
admin.site.register(CricketBoard)
admin.site.register(ICC)
admin.site.register(Player)
admin.site.register(Tournament)
admin.site.register(TeamOwner)
