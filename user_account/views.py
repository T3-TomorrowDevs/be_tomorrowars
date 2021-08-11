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
        """
        Handle every access, if is the signup, the class calls SignupAPIView, receives the response
        after the user creation, than sends the token in the response.
        """

        # store the access-token
        req_data = request.data

        # gets the user's data from google
        user_info = GoogleData.get_userinfo(req_data['access-token'])

        # store the googleid in a variable
        id_tmp = user_info["id"]

        # if the googleid not exists, call SignupAPIView
        if not UserAccount.objects.filter(google_id=id_tmp).exists():
            SignupAPIView.post(self, user_info=user_info)

        # get the user_id from database using the google_id (cannot use request.user because
        # the user is not logged in)
        user_id = UserAccount.objects.filter(google_id=id_tmp).values('user_id')[0]['user_id']

        # get the token using the user_id
        token = Token.objects.filter(user_id=user_id).values('key')[0]['key']

        return Response(token, status=status.HTTP_200_OK)


class SignupAPIView(APIView):

    def post(self, user_info):
        """
        Create the UserAccount record with googleid, the related user and the token.
        The token is generated automatically in the user_account/model.
        """

        # generate the username concatenating first_name+last_name+random_int
        username = "{}{}".format(user_info["name"], randrange(1, 1000))
        first_name = user_info["given_name"]
        last_name = user_info["family_name"]

        # create new account
        new_account = UserAccount()

        # create new related user
        new_account.user = User.objects.create_user(username, first_name=first_name,
                                            last_name=last_name)

        # store the googleid
        new_account.google_id = user_info["id"]

        new_account.save()

        return Response('Correctly registered', status=status.HTTP_201_CREATED)