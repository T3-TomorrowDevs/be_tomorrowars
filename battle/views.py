from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth.models import User

from shop.models import UserTroop  # troop model (troop_id)
from game.models import GameAccount  # game model (level and credit)

from battle.battle_utility.battle_output import BattleOutput
from battle.battle_utility.battle_algorithm import BattleAlgorithm
from battle.battle_utility.battle_utility import BattleUtility
from battle.serializers import BattleFightSerializer


class BattleSearchAPIView(APIView):

    # WE NEED TO UNDERSTAND HOW HANDLE THE TOKEN GIVEN BY THE SOCIAL

    # Specify what authentication to use, Requires token authentication
    # authentication_classes = [TokenAuthentication]
    # Will deny permission to any unauthenticated user, and allow permission otherwise
    # permission_classes = [IsAuthenticated]

    # return a list of id and level in a given range
    def get(self, request, *args, **kwargs):
        # user that is logged in
        user = request.user
        user_id = user.id

        # get the user level
        user_level = GameAccount.objects.filter(user=user_id).values_list('level')
        user_level = user_level[0][0]

        # get the min and max level based on the user level (range -+5)
        battle_utility = BattleUtility()
        min_level_range, max_level_range = battle_utility.filter_battle_search(user_id)

        # get a list of user-id and level in a given range
        # <QuerySet [(1, 1), (3, 3), (4, 1), (5, 7)]>
        id_level = GameAccount.objects.filter(level__gte=min_level_range, level__lte=max_level_range). \
            values_list('user', 'level')

        # perform the search fight output and exclude the id and level of the current user
        battle_out = BattleOutput()
        search_output = battle_out.battle_search_output(id_level, user_id)

        return Response(search_output, status=status.HTTP_200_OK)




class BattleFightAPIViews(APIView):

    # Specify what authentication to use
    # authentication_classes = [TokenAuthentication]  # Requires token authentication
    # Will deny permission to any unauthenticated user, and allow permission otherwise
    # permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):

        # from the request, extract the necessary information such as
        # enemy_id, enemy_multiplier, user_multiplier

        serializer = BattleFightSerializer(data=request.data)

        # if the fields format is correct
        if serializer.is_valid():
            # get the enemy id by the request data, <QueryDict: {'id': ['2']}>
            enemy_id = request.data['enemy_id']

            # user that is logged in
            user_id = request.user
            user_id = user_id.id

            enemy_multiplier = request.data['enemy_multiplier']
            user_multiplier = request.data['user_multiplier']

            # check if the enemy id exist in db
            if User.objects.filter(id=enemy_id).exists():

                # check if the enemy has troops
                if UserTroop.objects.filter(user=enemy_id).values_list('troop_id').exists():
                    enemy_troops = UserTroop.objects.filter(user=enemy_id).values_list('troop_id')

                    # check if the user has troops
                    if UserTroop.objects.filter(user=user_id).values_list('troop_id').exists():

                        # given all user troops
                        user_troops = UserTroop.objects.filter(user=user_id).values_list('troop_id')

                        # calculate who will win the battle given their troops and their multipliers
                        battle_algo = BattleAlgorithm(enemy_troops, user_troops, enemy_multiplier, user_multiplier)
                        result = battle_algo.get_battle_result()

                        # update the number of win/lose given the battle result
                        BattleFightAPIViews.update_win_lose(user_id, enemy_id, result)

                        # check if the number of win is a multiple of 5,
                        # if True update the level, else pass
                        BattleFightAPIViews.update_level(user_id, enemy_id, result)

                        # update winner level
                        if result['win']:
                            win = GameAccount.objects.get(user=user_id)
                            win = win.win

                            # if the number of win is a multiple of 5 return True, else False
                            bool_ = BattleUtility.check_number_of_win(win)

                            if bool_:
                                # update the level
                                level = GameAccount.objects.get(user=user_id)
                                update_level = level.level + 1
                                level.level = update_level
                                level.save()
                            else:
                                pass

                        return Response(result, status=status.HTTP_200_OK)

                    else:
                        # if the user has no troops
                        return Response('User has no troops', status.HTTP_400_BAD_REQUEST)

                else:
                    # if the enemy has no troops
                    return Response('Enemy has no troops', status.HTTP_400_BAD_REQUEST)

            else:
                # if the enemy id does not exists
                return Response('Enemy does not exists', status.HTTP_400_BAD_REQUEST)

        # if the format filed of the request data are not correct
        return Response("The field format is not correct, they must all be an integer", status.HTTP_400_BAD_REQUEST)


    @staticmethod
    def update_win_lose(user_id, enemy_id, result):

        if result['win']:
            winner = user_id
            loser = enemy_id
        else:
            winner = enemy_id
            loser = user_id

        # update the winner’s number of wins
        win = GameAccount.objects.get(user=winner)
        update_win = win.win + 1
        win.win = update_win
        win.save()

        # update the loser lose number
        lose = GameAccount.objects.get(user=loser)
        update_lose = lose.lose + 1
        lose.lose = update_lose
        lose.save()


    @staticmethod
    def update_level(user_id, enemy_id, result):

        if result['win']:
            winner = user_id
        else:
            winner = enemy_id

        win = GameAccount.objects.get(user=winner)
        win = win.win

        # if the number of win is a multiple of 5 return True, else False
        bool_ = BattleUtility.check_number_of_win(win)

        if bool_:
            # update the level
            level = GameAccount.objects.get(user=user_id)
            update_level = level.level + 1
            level.level = update_level
            level.save()
        else:
            pass