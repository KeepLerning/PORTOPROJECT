from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.dashboard, name='dashboard'),  # URL untuk halaman dashboard
    path('asset-list/', views.asset_list, name='asset_list'),
    path('asset-detail/<int:asset_id>/', views.asset_detail, name='asset_detail'),  # Menyertakan asset_id
    path('transactions/', views.transactions_view, name='transactions_view'),  # URL untuk transaksi
    path('transactions/', views.transactions, name='transactions'),  # URL untuk transaksi
    path('transactions/filter/', views.transaction_list_filter, name='transactions_filter'),  # URL filter transaksi dengan nama berbeda
]
