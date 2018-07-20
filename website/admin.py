from django import forms
from django.contrib import admin
from .models import Card
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


class CardAdminForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = '__all__'

    def clean(self):
        card_type = self.cleaned_data.get('card_type')
        if card_type == "Player":
            icc_ranking = self.cleaned_data.get('icc_ranking')
            country = self.cleaned_data.get('country')
            ipl_team = self.cleaned_data.get('ipl_team')
            if not icc_ranking:
                raise forms.ValidationError("Enter the ICC Ranking")
            if not country:
                raise forms.ValidationError("Enter the Country")
            if not ipl_team:
                raise forms.ValidationError("Enter the IPL Team")
        return self.cleaned_data


class CardAdmin(admin.ModelAdmin):
    form = CardAdminForm


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Card, CardAdmin)
