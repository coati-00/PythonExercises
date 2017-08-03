test_input = ['a', 'b', 'a', 'a']


def get_player_score(player, score, other):
    if score == 0:
        print player + " love"
    elif score == 1:
    	print player + " 15"
    elif score == 2:
    	print player  + " 30"
    else:
    	if score == 3 and other < 3 :
    		print player + " 40"
    	if score == other:
    	    print "Deuce"



def player_score(test_input):
    results = {'a': 0, 'b': 0}
    game_count = {'a': 0, 'b': 0}
    for point in test_input:
        results[point] = results[point] + 1
        if results[point] > 3:
        	game_count[point] = game_count[point] + 1
        	results['a'] = 0
        	results['b'] = 0
    print "Games " + str(game_count)
    print "current scores"
    get_player_score('a', results['a'], results['b'])
    get_player_score('b', results['b'], results['a'])
    

def test_player_score(player_list):
	print player_list
	player_score(player_list)
	print

test_player_score(test_input)
test_player_score([])
test_player_score(['a'])
test_player_score(['b'])
test_player_score(['a', 'b', 'a', 'b', 'a', 'a', 'a'])
test_player_score(list('aaaaaaaaaaaaaaaaaaaa'))
test_player_score(list('aaabbb'))
test_player_score(list('aaabbba'))
test_player_score(list('aaabbbaa'))