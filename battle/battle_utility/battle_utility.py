


class BattleUtility:

    @staticmethod
    def filter_battle_search(user_level):
        """
        given the current user level, returns a min and max level based on a given battle defined range
        """
        level_range = 5   # range of level for the battle (+-)

        max_level_range = level_range + user_level
        min_level_range = user_level - level_range

        # the min level must be 1
        if min_level_range < 1:
            min_level_range = 1

        return min_level_range, max_level_range


    @staticmethod
    def check_number_of_win(win):
        # if the number of win is a multiple of 5,
        # update the user level

        if win % 5 == 0:
            # the number is a multiple of 5
            return True
        else:
            # the number is not a multiple of 5
            return False

    @staticmethod
    def assign_credits_to_player(user_level):
        """ 
        set credit amounts based on level range
        assign defined amount to player in base of its level

        return :int number of credits
        """

        # set range level: every 5 levels 
        range_level = user_level // 5 

        # set initial credits' amount and perc bonus to assign
        START_CREDITS = 300
        BONUS_PERC = 30

        # set amount of credits to add to start credits
        bonus_credits = round(START_CREDITS * (BONUS_PERC / 100) * range_level) 

        # compute credits' amount to assign to playes based on range level
        assigned_credits = START_CREDITS + bonus_credits

        return assigned_credits
