from django.urls import path
from .views import *


urlpatterns = [
    path('', HomeView.as_view(), name='blog-home'),
    path('entry/<int:pk>/', EntryView.as_view(), name='entry_detail'),
    path('create_entry/', CreateEntryView.as_view(success_url='/'), name='create_entry'),
]