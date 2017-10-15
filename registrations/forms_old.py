from django import forms
from django.forms.models import inlineformset_factory
from .models import RegistrationPersonal, RegistrationAddress, RegistrationPayment


class PersonalForm(forms.ModelForm):
    class Meta:
        model = RegistrationPersonal
        fields = ('name','spousname','gender','kids','mobilenumber','email','bloodgroup','profession','organization' )


class AddressForm(forms.ModelForm):
    class Meta:
        model = RegistrationAddress
        fields = ('addserial', 'mobilenumber', 'address', 'postcode', 'thana', 'district', 'division', 'mate', 'spous', 'kids', 'guests', 'others', 'total', 'note')

class PaymentForm(forms.ModelForm):
    class Meta:
        model = RegistrationPayment
        fields = ('author', 'title')

BookFormSet = inlineformset_factory(RegistrationPersonal, RegistrationAddress, extra=0, min_num=1, fields=( 'mobilenumber', 'address', 'postcode', 'thana', 'district', 'division', 'mate', 'spous', 'kids', 'guests', 'others', 'total', 'note', ))