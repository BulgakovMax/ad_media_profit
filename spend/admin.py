from django.contrib import admin

from .models import SpendStatistic

class SpendStatisticAdmin(admin.ModelAdmin):
    list_display = ["name", "spend", "date", "impressions", "clicks", "conversion"]


admin.site.register(SpendStatistic, SpendStatisticAdmin)

