#  Copyright (c) 2020.  This repo or code maintained  by Sanjay kranthi
#  you can contact on this mail: kranthi0987@gmail.com
#  you can clone my projects git: github.com/kranthi0987

import uuid

from django.db import models


# Create your models here.

def my_random_string(string_length=10):
    """Returns a random string of length string_length."""
    random = str(uuid.uuid4())  # Convert UUID format to a Python string.
    random = random.upper()  # Make all characters uppercase.
    random = random.replace("-", "")  # Remove the UUID '-'.
    return random[0:string_length]  # Return the random string.


class UserModelData(models.Model):
    """ user model data which has the fields ID,
    Real_name,
    tz(location)
    """
    id = models.CharField(primary_key=True, default=my_random_string, max_length=50)
    real_name = models.TextField()
    tz = models.TextField()

    def __str__(self):
        return str(self.id)


class ActivityPeriodModels(models.Model):
    """Activity period model will have the start_time,
    end_time,
    user_id(foreign key of UserModelData)"""
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    user_id = models.ForeignKey('UserModelData', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user_id)
