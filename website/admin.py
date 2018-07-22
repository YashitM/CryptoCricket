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
        exclude = ('owner', 'last_bid',)

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
        if card_type == "Country":
            icc_ranking = self.cleaned_data.get('icc_ranking')
            if not icc_ranking:
                raise forms.ValidationError("Enter the ICC Ranking")
        return self.cleaned_data


# 0-Board; 1-Country; 2-Rest
class CardAdmin(admin.ModelAdmin):
    form = CardAdminForm

    def save_model(self, request, obj, form, change):
        card_type = form.cleaned_data['card_type']
        if card_type == "Board":
            obj.last_bid = 0.005
        elif card_type == "Country":
            obj.last_bid = 0.007
        else:
            obj.last_bid = 0.005

        super().save_model(request, obj, form, change)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Card, CardAdmin)
