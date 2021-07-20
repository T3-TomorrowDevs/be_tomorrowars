# perform the output of battle search


def battle_search_output(id, level):

    search_output = []

    for i in id:

        temp_ = {}

        temp_['id'] = i[0]

        for l in level:
            temp_['level'] = l[0]

        search_output.append(temp_)

    return search_output


"""
OUTPUT
[
{id:1,
level: 2},

{id:2
level: 5},

....

]
"""