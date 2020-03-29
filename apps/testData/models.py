import uuid

from django.db import models


# Create your models here.

def my_random_string(string_length=10):
    """Returns a random string of length string_length."""
    random = str(uuid.uuid4())  # Convert UUID format to a Python string.
    random = random.upper()  # Make all characters uppercase.
    random = random.replace("-", "")  # Remove the UUID '-'.
    return random[0:string_length]  # Return the random string.


print(my_random_string(6))


class UserModelData(models.Model):
    id = models.CharField(primary_key=True, default=my_random_string, max_length=50)
    real_name = models.TextField()
    tz = models.TextField()

    def __str__(self):
        return self.id


class ActivityPeriodModels(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    user_id = models.ForeignKey('UserModelData', null=True, db_column='purchase', blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.user_id
