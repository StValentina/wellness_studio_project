from django.urls import path

from studio_classes.views import StudioClassesCreateView

urlpatterns = [
    path('create', StudioClassesCreateView.as_view(), name='create-class'),
]
