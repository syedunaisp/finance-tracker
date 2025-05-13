from django import forms
from .models import Transaction

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['amount', 'category', 'type', 'date', 'account', 'transfer_to_account']
        exclude = ['user']

    category = forms.ChoiceField(choices=[...], required=True)  # Ensure required=True if it's a required field
    type = forms.ChoiceField(choices=[...], required=True)
    date = forms.DateField(required=True)
    account = forms.ModelChoiceField(queryset=Account.objects.all(), required=True)
    transfer_to_account = forms.ModelChoiceField(queryset=Account.objects.all(), required=False)