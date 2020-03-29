#  Copyright (c) 2020.  This repo or code maintained  by Sanjay kranthi
#  you can contact on this mail: kranthi0987@gmail.com
#  you can clone my projects git: github.com/kranthi0987

import faker
# Create your views here.
from django_seed import Seed
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.testData.models import UserModelData, ActivityPeriodModels
from apps.testData.serializer import UserDataModelSerialzier


class TestDataView(APIView):
    """
       It is used to ge the object list and through JSON response
       :param APIView:
       :return: Response of json
       """

    def get(self, request, *args, **kwargs):
        testmodel = UserModelData.objects.all()
        # the many param informs the serializer that it will be serializing more than a single article.
        serializer = UserDataModelSerialzier(testmodel, many=True)
        return Response({"ok": True, "members": serializer.data}, status=status.HTTP_200_OK)


@api_view(['POST'])
def DummyDataGenerator(APIView):
    """
    It is used to generate the dummy data to link the fields
    :param APIView:
    :return:
    """
    seeder = Seed.seeder()
    FAKE = faker.Faker()
    seeder.add_entity(UserModelData, 10, {
        'real_name': lambda x: FAKE.name(),
        'tz': lambda x: FAKE.address(),
    })
    seeder.add_entity(ActivityPeriodModels, 10)
    seeder.execute()
    return Response({"ok": True, "inserted": "Data inserted"}, status=status.HTTP_201_CREATED)
