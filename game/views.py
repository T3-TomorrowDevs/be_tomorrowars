from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import PlanetArmySerializer, GameAccountSerializer

from game.models import PlanetArmy



class PlanetArmyFormAPIView(APIView):

    """# Specify what authentication to use
    authentication_classes = [TokenAuthentication]  # Requires token authentication
    # Will deny permission to any unauthenticated user, and allow permission otherwise
    permission_classes = [IsAuthenticated]"""

    def post(self, request, *args, **kwargs):
        """
        method that accepts a request containing the name of the planet and the army chosen by the user.
        Save troop names in db table
        Save default level and credit values in table to db
        """

        # serializer
        planet_army_serializer = PlanetArmySerializer(data=request.data)  # handle incoming json requests

        # LEVEL AND CREDIT
        # at the moment, they are handle during the planet/army form
        # next time they will be managed immediately after registration
        # and this endpoint will be used for create or change army/planet name
        game_accounts_serializer = GameAccountSerializer(data=request.data)

        if game_accounts_serializer.is_valid():
            game_accounts_serializer.save(user=request.user)


        # get the planet and army name
        data = request.data
        planet = data['planet_name']
        army = data['army_name']


        # check if army name exists in db, false not exist, true exist
        if not PlanetArmy.objects.filter(army_name=army).exists():

            # check if planet name exists in db
            if not PlanetArmy.objects.filter(planet_name=planet).exists():

                # validate the input data and confirm that all required fields are correct
                if planet_army_serializer.is_valid():

                    # to save the object for the actual user
                    planet_army_serializer.save(user=request.user)

                    return Response("Name of planet and army added correctly.", status=status.HTTP_201_CREATED)

                return Response(planet_army_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


            else:
                return Response("Planet name already exists", status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response("Army name already exists", status=status.HTTP_400_BAD_REQUEST)
