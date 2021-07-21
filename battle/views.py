from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from game.models import GameAccount   # game model (level and credit)

from battle.battle_utility.battle_output import BattleOutput


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