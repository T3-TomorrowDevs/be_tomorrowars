from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import PlanetArmySerializer, GameAccountSerializer



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
        game_accounts_serializer = GameAccountSerializer(data=request.data)

        # validate the input data and confirm that all required fields are correct
        if planet_army_serializer.is_valid() and game_accounts_serializer.is_valid():

            # to save the object for the actual user
            game_accounts_serializer.save(user=request.user)
            planet_army_serializer.save(user=request.user)

            return Response("Name of planet and army added correctly.", status=status.HTTP_201_CREATED)
        return Response(planet_army_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
