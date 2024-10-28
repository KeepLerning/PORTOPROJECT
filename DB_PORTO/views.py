from django.shortcuts import render, get_object_or_404
from .models import Asset, Transaction

def asset_list(request):
    # Ambil semua aset dari database
    assets = Asset.objects.all()
    
    # Hitung perubahan nilai untuk setiap aset dan simpan hasilnya
    for asset in assets:
        if asset.initial_value:
            asset.change_percentage = ((asset.current_value - asset.initial_value) / asset.initial_value) * 100
        else:
            asset.change_percentage = 0  # Atau None, sesuai kebutuhan
    
    # Print untuk debug, memastikan data ada di assets
    print("Assets List:", assets)
    for asset in assets:
        print("Asset Name:", asset.asset_name, "Change %:", asset.change_percentage)
    
    # Render template dengan assets yang sudah termasuk change_percentage
    return render(request, 'asset_list.html', {'assets': assets})
    
def transaction_list(request):
    transactions = Transaction.objects.all()
    return render(request, 'transactions.html', {'transactions': transactions})

def asset_detail(request, asset_id):
    asset = get_object_or_404(Asset, id=asset_id)
    return render(request, 'asset_detail.html', {'asset': asset})

def transaction_list_filter(request):
    type_filter = request.GET.get('type')
    if type_filter:
        transactions = Transaction.objects.filter(type=type_filter)
    else:
        transactions = Transaction.objects.all()
    return render(request, 'transactions.html', {'transactions': transactions})
