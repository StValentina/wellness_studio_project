from django.urls import path

from studio_classes.views import StudioClassesCreateView, StudioClassesEditView, StudioClassesDeleteView, \
    TagsCreateView, TagsDeleteView, StudioClassesDetailsView

urlpatterns = [
    path('create', StudioClassesCreateView.as_view(), name='create-class'),
    path('edit/<int:pk>/', StudioClassesEditView.as_view(), name='edit-class'),
    path('delete/<int:pk>', StudioClassesDeleteView.as_view(), name='delete-class'),
    path('<int:pk>/details/', StudioClassesDetailsView.as_view(), name='details-class'),

    path('tag/create/', TagsCreateView.as_view(), name='create-tag'),
    path('tag/<int:pk>/delete/', TagsDeleteView.as_view(), name='delete-tag'),
]
