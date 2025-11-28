from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserBankAccount, UserAddress, User
from .constant import ACCOUNT_TYPE, GENDER_TYPE


class UserRegistrationForm(UserCreationForm):
    birth_date = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    gender = forms.ChoiceField(choices=GENDER_TYPE)
    account_type = forms.ChoiceField(choices=ACCOUNT_TYPE)
    street_address = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    postal_code = forms.IntegerField()
    country = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = [
            "username",
            "password1",
            "password2",
            "first_name",
            "last_name",
            "email",
            "account_type",
            "birth_date",
            "gender",
            "postal_code",
            "city",
            "country",
            "street_address",
        ]

    def save(self, commit=True):
        our_user = super().save(commit=False)
        if commit == True:
            our_user.save()
            account_type = self.cleaned_data.get("account_type")
            gender = self.cleaned_data.get("gender")
            postal_code = self.cleaned_data.get("postal_code")
            country = self.cleaned_data.get("country")
            birth_date = self.cleaned_data.get("birth_date")
            city = self.cleaned_data.get("city")
            street_address = self.cleaned_data.get("street_address")

            UserAddress.objects.create(
                user=our_user,
                street_address=street_address,
                city=city,
                postal_code=postal_code,
                country=country,
            )

            UserBankAccount.objects.create(
                user=our_user,
                account_type=account_type,
                birth_date=birth_date,
                gender=gender,
                account_no=our_user.id + 100000,
            )
            return our_user
