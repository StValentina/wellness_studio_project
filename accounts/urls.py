from django.urls import path
from accounts.views import RegisterView, LoginUserView, logout_user

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
]