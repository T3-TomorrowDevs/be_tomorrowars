# class that takes care of reformatting the outputs inherent in the battle app

class BattleOutput:

    @staticmethod
    def battle_search_output(id_level, user_id):
        """
        given a queryset object like [(3, 3), (5, 7)]
        where the first value of array is the id and the second the level

        return a dict more clean like
        [{'id': 3, 'level': 3},
        {'id': 5, 'level': 7}]
        """
        search_out = []

        for i in id_level:
            # to exclude the current user id and level
            if i[0] == user_id:
                pass
            else:
                temp = {'id': i[0], 'level': i[1]}
                search_out.append(temp)


        return search_out