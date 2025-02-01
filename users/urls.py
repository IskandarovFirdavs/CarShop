from django.contrib.auth.views import LogoutView
from django.urls import path

from users.views import registration_view, login_view, profile_view

app_name = 'users'

urlpatterns = [
    path('', registration_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page='/login/'), name='logout'),
    path('profile/', profile_view, name='profile'),
]
