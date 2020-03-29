#  Copyright (c) 2020.  This repo or code maintained  by Sanjay kranthi
#  you can contact on this mail: kranthi0987@gmail.com
#  you can clone my projects git: github.com/kranthi0987

from django.urls import path

from apps.testData.views import TestDataView, DummyDataGenerator

urlpatterns = [
    path('getdata/', TestDataView.as_view()),
    path('createDummydata/', DummyDataGenerator)
]
