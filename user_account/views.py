from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import status  # for send status
from rest_framework.views import APIView  # class view

import user_account.models
from user_account.google_account.handle_google_data import GoogleData
from .models import UserAccount
from django.contrib.auth.models import User
from random import randrange
from rest_framework.authtoken.models import Token
import json


class LoginAPIView(APIView):

    def post(self, request):
        req_data = request.data

        user_info = GoogleData.get_userinfo(req_data['access-token'])
        id_tmp = user_info["id"]

        if not UserAccount.objects.filter(google_id=id_tmp).exists():
            SignupAPIView.post(self, user_info=user_info)

        user_id = UserAccount.objects.filter(google_id=id_tmp).values('user_id')[0]['user_id']
        token = Token.objects.filter(user_id=user_id).values('key')[0]['key']
        print(token)

        return Response(json.loads('Token: {}'.format(token)), status=status.HTTP_200_OK)


class SignupAPIView(APIView):

    def post(self, user_info):
        username = "{}{}".format(user_info["name"], randrange(1, 1000))
        first_name = user_info["given_name"]
        last_name = user_info["family_name"]

        new_account = UserAccount()
        new_account.user = User.objects.create_user(username, first_name=first_name,
                                            last_name=last_name)

        new_account.google_id = user_info["id"]
        new_account.save()

        return Response('Correctly registered', status=status.HTTP_201_CREATED)