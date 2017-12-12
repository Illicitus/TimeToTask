from django.contrib import admin

from api.models import Statistics


class StatisticsAdmin(admin.ModelAdmin):
    def time_seconds(self, obj):
        """
        Change data format to '%d-%m-%Y'.
        """
        return obj.date.strftime("%d-%m-%Y")

    time_seconds.admin_order_field = 'date'
    time_seconds.short_description = 'Precise Time'

    list_display = ('time_seconds', 'url', 'access_count')
    list_filter = ('date', 'url')
    readonly_fields = ('url', 'access_count')


admin.site.register(Statistics, StatisticsAdmin)
