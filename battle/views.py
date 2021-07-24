from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from shop.models import UserTroop     # troop model (troop_id)
from game.models import GameAccount   # game model (level and credit)

from battle.battle_utility.battle_output import BattleOutput
from battle.battle_utility.battle_algorithm import BattleAlgorithm


class BattleSearchAPIView(APIView):

    # WE NEED TO UNDERSTAND HOW HANDLE THE TOKEN GIVEN BY THE SOCIAL

    # Specify what authentication to use, Requires token authentication
    #authentication_classes = [TokenAuthentication]
    # Will deny permission to any unauthenticated user, and allow permission otherwise
    #permission_classes = [IsAuthenticated]


    # return a list of ALL user and level
    def get(self, request, *args, **kwargs):

        id = GameAccount.objects.all().values_list('id')
        level = GameAccount.objects.all().values_list('level')

        battle_out = BattleOutput()
        search_output = battle_out.battle_search_output(id, level)

        return Response(search_output, status=status.HTTP_200_OK)



class BattleFightAPIViews(APIView):

    # Specify what authentication to use
    #authentication_classes = [TokenAuthentication]  # Requires token authentication
    # Will deny permission to any unauthenticated user, and allow permission otherwise
    #permission_classes = [IsAuthenticated]


    def post(self, request, *args, **kwargs):

        # from the request, extract the necessary information such as
        # enemy_id, enemy_multiplier, user_multiplier

        # get the enemy id by the request data, <QueryDict: {'id': ['2']}>
        enemy_id = request.data['enemy_id']

        # user that is logged in
        user = request.user
        user_id = user.id

        enemy_multiplier = request.data['enemy_multiplier']
        user_multiplier = request.data['user_multiplier']

        # for the user and enemy given their id, get all their troops
        user_troops = UserTroop.objects.filter(user=user_id).values_list('troop_id')

        enemy_troops = UserTroop.objects.filter(user=enemy_id).values_list('troop_id')

        # calculate who will win the battle given their troops and their multipliers
        battle_algo = BattleAlgorithm(enemy_troops, user_troops, enemy_multiplier, user_multiplier)
        result = battle_algo.get_battle_result()

        return Response(result, status=status.HTTP_200_OK)