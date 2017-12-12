from django.contrib import admin

from api.models import Statistics


class StatisticsAdmin(admin.ModelAdmin):
    def date_format(self, obj):
        """
        Changes data format to '%d-%m-%Y'.
        """
        return obj.date.strftime("%d-%m-%Y")

    date_format.admin_order_field = 'date'
    date_format.short_description = 'Precise Time'

    list_display = ('date_format', 'url', 'access_count')
    list_filter = ('date', 'url')
    readonly_fields = ('url', 'access_count')


admin.site.register(Statistics, StatisticsAdmin)
