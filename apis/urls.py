from django.urls import path, include
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required

from rest_framework import permissions

urlpatterns = [
    path('auth/', include('accounts.urls')),
    path('', include('category.urls', namespace='categories')),
    path('', include('product.urls', namespace='product')),
]
