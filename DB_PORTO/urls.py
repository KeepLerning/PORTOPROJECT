from django.urls import path
from .views import asset_list, transaction_list_filter, asset_detail  # Gunakan view yang benar

urlpatterns = [
    path('assets/', asset_list, name='asset_list'),
    path('transactions/', transaction_list_filter, name='transactions'),  # Menggunakan transaction_list_filter sebagai transaction_list
    path('assets/<int:asset_id>/', asset_detail, name='asset_detail'),
]
