import faker
from django.shortcuts import render

# Create your views here.
from django_seed import Seed
from faker.generator import random
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.testData.models import UserModelData, ActivityPeriodModels
from apps.testData.serializer import UserDataModelSerialzier


class TestDataView(APIView):
    def get(self, request, *args, **kwargs):
        testmodel = UserModelData.objects.all()
        # the many param informs the serializer that it will be serializing more than a single article.
        serializer = UserDataModelSerialzier(testmodel, many=True)
        return Response({"ok": True, "members": serializer.data}, status=status.HTTP_200_OK)


@api_view(['POST'])
def DummyDataGenerator(APIView):
    seeder = Seed.seeder()
    FAKE = faker.Faker()
    seeder.add_entity(UserModelData, 10, {
        'real_name': lambda x: FAKE.name(),
        'tz': lambda x:  FAKE.address(),
    })
    seeder.add_entity(ActivityPeriodModels, 10)
    inserted_pks = seeder.execute()
    return Response({"ok": True, "inserted": "inserted_pks"}, status=status.HTTP_201_CREATED)
