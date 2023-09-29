from rest_framework import generics
from django.db.models import Sum
from .models import SpendStatistic
from .serializers import SpendStatisticSerializer

class SpendStatisticListView(generics.ListAPIView):
    serializer_class = SpendStatisticSerializer

    def get_queryset(self):
        queryset = SpendStatistic.objects.values('name', 'date').annotate(
            total_spend=Sum('spend'),
            total_impressions=Sum('impressions'),
            total_clicks=Sum('clicks'),
            total_conversion=Sum('conversion'),
            revenue_amount=Sum('revenuestatistic__revenue')
        )
        return queryset
