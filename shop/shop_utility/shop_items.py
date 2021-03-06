""" 
dictionary for troops symbolic values
"""

class ShopTroops:

    shop_troops = {
        1: {
            'troop_id': 1,
            'troop_name': 'troop_1',
            'troop_level': 1,
            'troop_cost': 100,
            'troop_att': 50,
            'troop_def': 50},

        2: {
            'troop_id': 2,
            'troop_name': 'troop_2',
            'troop_level': 1,
            'troop_cost': 110,
            'troop_att': 60,
            'troop_def': 40},

        3: {
            'troop_id': 3,
            'troop_name': 'troop_3',
            'troop_level': 2,
            'troop_cost': 120,
            'troop_att': 60,
            'troop_def': 50},

        4: {
            'troop_id': 4,
            'troop_name': 'troop_4',
            'troop_level': 2,
            'troop_cost': 130,
            'troop_att': 60,
            'troop_def': 60},

        5: {
            'troop_id': 5,
            'troop_name': 'troop_5',
            'troop_level': 3,
            'troop_cost': 140,
            'troop_att': 70,
            'troop_def': 60},

        6: {
            'troop_id': 6,
            'troop_name': 'troop_6',
            'troop_level': 3,
            'troop_cost': 150,
            'troop_att': 70,
            'troop_def': 70},

        7: {
            'troop_id': 7,
            'troop_name': 'troop_7',
            'troop_level': 4,
            'troop_cost': 160,
            'troop_att': 80,
            'troop_def': 70},

        8: {
            'troop_id': 8,
            'troop_name': 'troop_8',
            'troop_level': 4,
            'troop_cost': 170,
            'troop_att': 80,
            'troop_def': 80},

        9: {
            'troop_id': 9,
            'troop_name': 'troop_9',
            'troop_level': 5,
            'troop_cost': 180,
            'troop_att': 90,
            'troop_def': 80},

        10: {
            'troop_id': 10,
            'troop_name': 'troop_10',
            'troop_level': 5,
            'troop_cost': 190,
            'troop_att': 100,
            'troop_def': 100}
    }

    # method to query the shop_troop dict
    @staticmethod
    def get_troop_value(troop_id, troop_value):

        # get dict into variable
        troops = ShopTroops.shop_troops

        # guard structure to validate appropriate params        
        if troop_id < 1 or troop_id > len(troops):
            print("wrong troop_id")
            quit()

        for troop in troops:

            if troop_value not in troops[troop]:
                print("wrong troop_value")
                quit()


        # return data from dict
        return troops[troop_id][troop_value]



