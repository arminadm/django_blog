from django.urls import path
from accounts.views import *

app_name = 'accounts'

urlpatterns = [
    # Login
    path('login/', login_view, name='login'),
    # Logout
    path('logout/', logout_view, name='logout')
    # Singup
]