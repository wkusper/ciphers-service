
from django.urls import path
from .views import greetings
from .views import encode

urlpatterns = [
    path('', greetings),
    path('caesar/<str:plaintext>/<int:shift>/', encode),
]