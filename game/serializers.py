from rest_framework.serializers import ModelSerializer
from .models import PlanetArmy, GameAccount


class PlanetArmySerializer(ModelSerializer):

    class Meta:
        model = PlanetArmy       # model to serialize
        fields = ['planet_name', 'army_name']  # How many fields to display ("__all__")


class GameAccountSerializer(ModelSerializer):

    class Meta:
        model = GameAccount   # model to serialize
        fields = ['level', 'credit']