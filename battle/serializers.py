from rest_framework import serializers


class BattleFightSerializer(serializers.Serializer):
    # declares the types of fields
    enemy_id = serializers.IntegerField()
    enemy_multiplier = serializers.IntegerField()
    user_multiplier = serializers.IntegerField()
