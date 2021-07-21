# class that takes care of reformatting the outputs inherent in the battle app

class BattleOutput:

    def battle_search_output(self, id, level):
        """
        :param id: <QuerySet [(1,), (2,), (3,), (4,), (5,)]>
        :param level: <QuerySet [(1,), (1,), (1,), (1,), (1,)]>

        reformat the output to make it clearer, it will be:
        [
            {"id": 1,
            "level": 1},

            {"id": 2,
            "level": 1}
        ]
        """

        search_output = []

        for i in id:

            temp_ = {}
            temp_['id'] = i[0]

            for l in level:
                temp_['level'] = l[0]

            search_output.append(temp_)

        return search_output
