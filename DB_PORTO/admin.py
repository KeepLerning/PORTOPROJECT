from django.contrib import admin
from .models import User, Asset, Transaction

admin.site.register(User)
admin.site.register(Asset)
admin.site.register(Transaction)
