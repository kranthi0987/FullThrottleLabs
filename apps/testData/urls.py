from django.conf.urls import url
from django.urls import path

from apps.testData.views import TestDataView, DummyDataGenerator

urlpatterns = [
    path('getdata/', TestDataView.as_view()),
    path('createDummydata/',DummyDataGenerator)
]