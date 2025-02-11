from django.urls import path
from blog.views import post_details  

app_name = 'blog'

urlpatterns = [
    path('details/<int:id>/', post_details, name='details'),  
]
