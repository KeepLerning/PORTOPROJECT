from django.shortcuts import render, get_object_or_404, redirect
from DB_PORTO.models import Asset, Transaction
from DB_PORTO.forms import TransactionForm

# View untuk halaman Dashboard
def dashboard(request):
    return render(request, 'dashboard.html')

# View untuk Daftar Aset
def asset_list(request):    
    assets = Asset.objects.all()
    for asset in assets:
        if asset.initial_value:
            asset.change_percentage = ((asset.current_value - asset.initial_value) / asset.initial_value) * 100
        else:
            asset.change_percentage = 0
    
    print(assets)  # Tambahkan ini untuk memeriksa apakah aset diambil dengan benar
    return render(request, 'asset_list.html', {'assets': assets})

# View untuk Detail Aset
def asset_detail(request, asset_id):
    asset = get_object_or_404(Asset, id=asset_id)
    return render(request, 'asset_detail.html', {'asset': asset})

# View untuk Daftar Transaksi
def transactions(request):
    transactions = Transaction.objects.all()  # Ambil semua transaksi untuk halaman ini
    return render(request, 'transactions.html', {'transactions': transactions})

def transactions_view(request):
    assets = Asset.objects.all()

    if request.method == 'POST':
        asset_id = request.POST.get('asset')
        transaction_type = request.POST.get('type')
        amount = float(request.POST.get('amount'))  # Konversi ke float

        # Temukan aset berdasarkan ID
        try:
            asset = Asset.objects.get(id=asset_id)

            # Buat dan simpan transaksi
            transaction = Transaction(asset=asset, type=transaction_type, amount=amount)
            transaction.save()

            # Update jumlah aset sesuai jenis transaksi
            if transaction_type == 'purchase':
                asset.quantity += amount  # Tambahkan sesuai jumlah
            elif transaction_type == 'sale':
                asset.quantity -= amount  # Kurangi sesuai jumlah

            asset.save()  # Simpan perubahan aset

            return redirect('transactions')  # Redirect setelah simpan

        except Asset.DoesNotExist:
            # Jika aset tidak ditemukan
            return render(request, 'transactions.html', {'assets': assets, 'error': 'Aset tidak ditemukan.'})

    return render(request, 'transactions.html', {'assets': assets})

# View untuk Filter Transaksi
def transaction_list_filter(request):
    type_filter = request.GET.get('type', '')
    date_filter = request.GET.get('date', '')

    # Membangun queryset berdasarkan filter yang diberikan
    transactions = Transaction.objects.all()

    if type_filter:
        # Filter menggunakan `__icontains` untuk pencarian yang tidak sensitif terhadap huruf besar/kecil
        transactions = transactions.filter(type__icontains=type_filter)

    if date_filter:
        transactions = transactions.filter(date__date=date_filter)

    return render(request, 'transactions.html', {'transactions': transactions})

def create_transaction(request):
    if request.method == "POST":
        # Proses form submission
        asset_id = request.POST.get('asset')
        transaction_type = request.POST.get('type')
        amount = float(request.POST.get('amount'))  # Konversi ke float

        asset = Asset.objects.get(id=asset_id)
        transaction = Transaction(asset=asset, type=transaction_type, amount=amount)
        transaction.save()

        # Update jumlah aset berdasarkan jenis transaksi
        if transaction.type == 'purchase':
            asset.quantity += amount
        elif transaction.type == 'sale':
            asset.quantity -= amount
        asset.save()  # Simpan perubahan pada aset

        return redirect('transactions')  # Ganti dengan URL yang sesuai
    else:
        # Mengambil semua aset untuk ditampilkan di form
        assets = Asset.objects.all()
        return render(request, 'transactions.html', {'assets': assets})
