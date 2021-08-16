from rest_framework.serializers import ModelSerializer
from game.models import UserTroop


class UserTroopSerializer(ModelSerializer):

    class Meta:
        model = UserTroop       # model to serialize

        fields = ['troop_id']  # How many fields to display ("__all__")
