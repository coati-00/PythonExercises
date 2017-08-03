'''Given an old phone keypad, determine how to get all possible
combinations of letters for combinations of two keys'''

digits_to_letters = {"1": "",
                     "2": "abc",
                     "3": "def",
                     "4": "ghi",
                     "5": "jkl",
                     "6": "mno",
                     "7": "pqrs",
                     "8": "tuv",
                     "9": "wxyz",
                    }

def get_letter_combos(number_combo):
    num_com = str(number_combo)
    #digits = len(num_com)
    hold_combs = []
    for first_num in num_com:
        letters = digits_to_letters[num]
        for first_num in num_com:




