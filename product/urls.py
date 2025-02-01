from django.urls import path
from product.views import details, home

app_name = 'product'

urlpatterns = [
    path('', home, name='home'),
    path('details/<int:id>/', details, name='details'),
]
