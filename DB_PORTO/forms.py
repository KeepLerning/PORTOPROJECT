from django import forms
from .models import Transaction, Asset

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['asset', 'type', 'amount']

    asset = forms.ModelChoiceField(queryset=Asset.objects.all(), label="Pilih Aset")
    type = forms.ChoiceField(choices=[('purchase', 'Pembelian'), ('sale', 'Penjualan')], label="Jenis Transaksi")
    amount = forms.DecimalField(label="Jumlah", min_value=0)
