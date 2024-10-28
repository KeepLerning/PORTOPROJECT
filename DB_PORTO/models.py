from django.db import models

class User(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

class Asset(models.Model):
    asset_name = models.CharField(max_length=255)
    value = models.DecimalField(max_digits=15, decimal_places=2)
    category = models.CharField(max_length=100)
    initial_value = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)  # Nilai awal
    current_value = models.DecimalField(max_digits=15, decimal_places=2)  # Nilai saat ini
    quantity = models.IntegerField(default=1)  # Menyimpan jumlah aset

    def __str__(self):
        return self.asset_name

class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('purchase', 'Pembelian'),
        ('sale', 'Penjualan'),
    )
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=15, decimal_places=2)  # Pastikan ini adalah DecimalField

    def save(self, *args, **kwargs):
        # Update jumlah aset ketika transaksi disimpan
        if self.type == 'purchase':
            self.asset.quantity += self.amount  # Tambah jumlah aset
        elif self.type == 'sale':
            self.asset.quantity -= self.amount  # Kurangi jumlah aset
        self.asset.save()  # Simpan perubahan pada aset
        super().save(*args, **kwargs)  # Panggil metode save dari superclass

    def __str__(self):
        return f"{self.type} - {self.asset.asset_name} on {self.date.strftime('%Y-%m-%d')}"
