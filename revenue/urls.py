from django.urls import path
from .views import RevenueStatisticListView

urlpatterns = [
    path('revenue-statistics/', RevenueStatisticListView.as_view(), name='revenue-statistics'),
]
