from shop.shop_utility.shop_items import ShopTroops



class BattleAlgorithm:

    def __init__(self, enemy_troops_id, user_troops_id, enemy_multiplier, user_multiplier):
        """
        The parameters enemy_troops_id and user_troops_id are QuerySet object, like:
        <QuerySet [(1,), (1,), (2,)]>

        I turn both in list through a list comprehension to be more easily manageable
        """

        self.enemy_multiplier = enemy_multiplier
        self.user_multiplier = user_multiplier

        self.enemy_troops_values = BattleAlgorithm.get_troop_values([i[0] for i in enemy_troops_id])
        self.user_troops_values = BattleAlgorithm.get_troop_values([i[0] for i in user_troops_id])


    @staticmethod
    def get_troop_values(troops_id):
        """
        given a list of id, return a dict with the id and the values of each troop

        {'id': [1, 1, 2],
        'att': [50, 50, 60],
        'def': [70, 70, 40]}
        """

        troops_values = {'id': troops_id, 'att': [], 'def': []}

        # fill the created dict with the corresponding values for each given troop id
        for i in troops_id:
            troops_values['att'].append(ShopTroops.get_troop_value(i, 'troop_att'))
            troops_values['def'].append(ShopTroops.get_troop_value(i, 'troop_def'))

        return troops_values


    def get_battle_result(self):

        """
        :return
        {'win': bool,   True if user win, else False
         'rest_def': int,
         'total_def': int}
        """

        # for the user and the enemy, sum the values of attack and defense of all troops
        # finally multiplies by your own multiplier
        enemy_att = sum(self.enemy_troops_values['att']) * self.enemy_multiplier
        enemy_def = sum(self.enemy_troops_values['def']) * self.enemy_multiplier

        user_att = sum(self.user_troops_values['att']) * self.user_multiplier
        user_def = sum(self.user_troops_values['def']) * self.user_multiplier

        # choose random who starts attacking, to implement in the milestone 2
        # who_start = random.choice(['enemy', 'user'])

        # get the difference of the values
        rest_enemy_def = enemy_def - user_att
        rest_user_def = user_def - enemy_att


        # compare the defense values left after the battle
        # if the user defense win
        if rest_user_def > rest_enemy_def:
            return {'win': True, 'rest_def': rest_user_def, 'total_def': user_def}

        else:
            return {'win': False, 'rest_def': rest_enemy_def, 'total_def': enemy_def}
