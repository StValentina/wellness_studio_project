from django.urls import path

from reviews.views import ReviewCreateView, ReviewDeleteView, ReviewEditView
from studio_classes.views import ClassReviewListView

urlpatterns = [
    path('create/<int:pk>/', ReviewCreateView.as_view(), name='create-review'),
    path('<int:pk>/edit/', ReviewEditView.as_view(), name='edit-review'),
    path('<int:pk>/delete/', ReviewDeleteView.as_view(), name='delete-review'),
    path('class/<int:pk>/', ClassReviewListView.as_view(), name='class-reviews'),
]