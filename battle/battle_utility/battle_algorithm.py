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
