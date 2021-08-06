from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import status  # for send status
from rest_framework.views import APIView  # class view
from user_account.google_account.handle_google_data import GoogleData
from .models import UserAccount
from django.contrib.auth.models import User
from random import randrange


class LoginAPIView(APIView):

    def post(self, request):
        req_data = request.data

        user_info = GoogleData.get_userinfo(req_data['access-token'])

        username = "{}{}".format(user_info["name"], randrange(1, 1000))
        first_name = user_info["given_name"]
        last_name = user_info["family_name"]

        new_account = UserAccount()
        new_account.user = User.objects.create_user(username, first_name=first_name,
                                            last_name=last_name)

        new_account.google_id = user_info["id"]
        new_account.save()

        return Response('Correctly registered', status=status.HTTP_201_CREATED)


