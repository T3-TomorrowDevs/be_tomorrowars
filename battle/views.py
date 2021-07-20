from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from game.models import GameAccount   # game model (level and credit)

from game.game_utility.battle_search_output import battle_search_output


class BattleSearchAPIView(APIView):

    # WE NEED TO UNDERSTAND HOW HANDLE THE TOKEN GIVEN BY THE SOCIAL

    # Specify what authentication to use, Requires token authentication
    #authentication_classes = [TokenAuthentication]
    # Will deny permission to any unauthenticated user, and allow permission otherwise
    #permission_classes = [IsAuthenticated]


    # to return the list of all user level
    def get(self, request, *args, **kwargs):

        id = GameAccount.objects.all().values_list('id')
        level = GameAccount.objects.all().values_list('level')

        search_output = battle_search_output(id, level)

        return Response(search_output, status=status.HTTP_200_OK)