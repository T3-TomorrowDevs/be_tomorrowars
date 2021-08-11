from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from shop.shop_utility.shop_items import ShopTroops



class ShopAPIView(APIView):
    # Specify what authentication to use
    authentication_classes = [TokenAuthentication]  # Requires token authentication
    # Will deny permission to any unauthenticated user, and allow permission otherwise
    permission_classes = [IsAuthenticated]

    # to return the list of items available
    def get(self, request, *args, **kwargs):
        """
        the response will be like
            {
        "1": {
            "troop_id": 1,
            "troop_name": "troop_1",
            "troop_level": 1,
            "troop_cost": 100,
            "troop_att": 50,
            "troop_def": 50
        },
        "2": {
            "troop_id": 2,
            "troop_name": "troop_2",
            "troop_level": 1,
            "troop_cost": 110,
            "troop_att": 60,
            "troop_def": 40
        }},

        """

        return Response(ShopTroops.shop_troops, status=status.HTTP_200_OK)