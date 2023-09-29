from django.urls import path
from .views import SpendStatisticListView

urlpatterns = [
    path('spend-statistics/', SpendStatisticListView.as_view(), name='spend-statistics'),
]
