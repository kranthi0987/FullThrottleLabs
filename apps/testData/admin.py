#  Copyright (c) 2020.  This repo or code maintained  by Sanjay kranthi
#  you can contact on this mail: kranthi0987@gmail.com
#  you can clone my projects git: github.com/kranthi0987

from django.contrib import admin
# Register your models here.
from django.db import models

from apps.testData.models import UserModelData, ActivityPeriodModels


# admin.site.register(UserModelData)
# admin.site.register(ActivityPeriodModels)


# ModelAdmin Class # DataFlair
class UserModelData1(admin.ModelAdmin):
    list_display = ('id', 'real_name', 'tz',)
    list_filter = ('id',)
    formfield_overrides = {
        models.DateTimeField: {'input_formats': ('%b %d %Y',)},
    }


class ActivityPeriodModels1(admin.ModelAdmin):
    list_display = ('user_id', 'start_time', 'end_time',)
    list_filter = ('start_time', 'end_time', 'user_id')
    formfield_overrides = {
        models.DateTimeField: {'input_formats': ('%b %d %Y',)},
    }

# admin.site.register(Groups)
# admin.site.register(Users)
admin.site.register(UserModelData, UserModelData1)
admin.site.register(ActivityPeriodModels, ActivityPeriodModels1)

admin.site.site_header = "Full Throttle Labs Django Admin"
