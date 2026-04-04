from django.urls import path, include
from accounts.views import RegisterView, LoginUserView, logout_user, AccountDetailView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('', include([
        path('<int:pk>/detail/', AccountDetailView.as_view(), name='profile_detail'),
    ]))
]