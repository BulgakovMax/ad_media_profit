from rest_framework import serializers
from .models import SpendStatistic

class SpendStatisticSerializer(serializers.ModelSerializer):
    
    name = serializers.CharField(max_length=255)
    date = serializers.DateField()
    total_spend = serializers.DecimalField(max_digits=10, decimal_places=2)
    total_impressions = serializers.IntegerField()
    total_clicks = serializers.IntegerField()
    total_conversion = serializers.IntegerField()
    revenue_amount = serializers.DecimalField(max_digits=9, decimal_places=2)

    class Meta:
        model = SpendStatistic
        fields = ('name', 'date', 'total_spend', 'total_impressions', 'total_clicks', 'total_conversion', 'revenue_amount')
