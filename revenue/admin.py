from django.contrib import admin

from .models import RevenueStatistic


class RevenueStatisticAdmin(admin.ModelAdmin):
    list_display = ["name", "spend", "date", "revenue"]


admin.site.register(RevenueStatistic, RevenueStatisticAdmin)
