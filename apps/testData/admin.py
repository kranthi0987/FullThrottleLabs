from django.contrib import admin

# Register your models here.
from apps.testData.models import UserModelData, ActivityPeriodModels


# admin.site.register(UserModelData)
# admin.site.register(ActivityPeriodModels)


# ModelAdmin Class # DataFlair
class UserModelData1(admin.ModelAdmin):
    list_display = ('id', 'real_name', 'tz',)
    list_filter = ('id',)


class ActivityPeriodModels1(admin.ModelAdmin):
    list_display = ('user_id', 'start_time', 'end_time',)
    list_filter = ('start_time','end_time','user_id')

# admin.site.register(Groups)
# admin.site.register(Users)
admin.site.register(UserModelData, UserModelData1)
admin.site.register(ActivityPeriodModels, ActivityPeriodModels1)

admin.site.site_header = "Full Throttle Labs Django Admin"
