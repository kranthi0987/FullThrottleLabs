#  Copyright (c) 2020.  This repo or code maintained  by Sanjay kranthi
#  you can contact on this mail: kranthi0987@gmail.com
#  you can clone my projects git: github.com/kranthi0987

# Generated by Django 3.0.4 on 2020-03-29 11:35

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('testData', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodeldata',
            name='id',
            field=models.UUIDField(default=uuid.UUID('37a9d44e-6025-4ac2-bd50-2f0de1525834'), primary_key=True, serialize=False),
        ),
    ]
