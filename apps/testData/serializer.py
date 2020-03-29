from rest_framework import serializers

from apps.testData.models import UserModelData, ActivityPeriodModels


class UserDataModelSerialzier(serializers.ModelSerializer):
    class Meta:
        model = UserModelData
        fields = '__all__'

    def to_representation(self, instance):
        ret = super(UserDataModelSerialzier, self).to_representation(instance)
        # check the request is list view or detail view
        is_list_view = isinstance(self.instance, list)
        id = ret.get('id')
        activtymodel = ActivityPeriodModels.objects.filter(user_id=id)
        activity_periods_array = []
        activity_periods_total = {'activity_periods': activity_periods_array}
        print(activtymodel.count())
        for modells in activtymodel:
            if modells is None:
                activity_periods = {"start_time": "no",
                                    "end_time": "no"}
                activity_periods_array.append(activity_periods)
            else:
                activity_periods = {"start_time": modells.start_time,
                                    "end_time": modells.end_time}
                activity_periods_array.append(activity_periods)

        # extra_ret = {'key': 'list value'} if is_list_view else {'key': 'single value'}
        ret.update(activity_periods_total)
        return ret
