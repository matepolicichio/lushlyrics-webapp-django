from django.urls import path
from .views import UserRegisterView

app_name = 'accounts'
urlpatterns = [
    path('signup/', UserRegisterView.as_view(), name='signup'),
]
