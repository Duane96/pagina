from django.urls import path
from .views import *


urlpatterns = [
    path('', inicioes, name="inicioes"),
    path('en/', inicioen, name="inicioen"),
]
