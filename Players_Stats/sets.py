import json

player_name='Djokovic N.'
year='2023'
tournament_name='European Open'
location = 'Hamburg'
best_of='3'

"""
Only the best of 3 sets
    Of all time
	During the year
	In the tournament 
	H2h

	Get matches won in consecutive sets 
	Get matches won when the player win the first set
	Get matches won in 3 sets 
    Get matches won  in 3 sets when the player win the first set 
	Get matches won in 3 sets when the player loss the first set 

Only the best of 5 sets

    Of all time
	During the year
	In the tournament 
    H2h

	Get matches won in consecutive sets 
	Get matches won in 4 sets 
	Get matches won in 5 sets 
    Get matches won when the player win the first set
    Get matches won when the player win the first two sets
    Get matches won  in 4 sets when the player loss the first set
    Get matches won  in 4 sets when the player win the first two sets
    Get matches won  in 4 sets when the player loss the second set


    Get matches won  in 5 sets when the player win the first set
    Get matches won  in 5 sets when the player win the first two sets
    Get matches won  in 5 sets when the player loss the first set
    Get matches won  in 5 sets when the player loss the first two sets
    Get matches won  in 5 sets when the player win the first and third set
    Get matches won  in 5 sets when the player loss the first and third set

"""
#Get matches won in consecutive set
def Consecutive_sets(year, player_name, best_of):
    file = open('../JSON_files/ResultATP_'+year+'.json')
    data = json.load(file)
    player= {"Win":0, "Loss":0}

    # Get the player wins and loss

    if best_of == "3":
        for info in data:

            if info['Winner'] == player_name and info['Best of'] == best_of:
                if info['W1'] > info['L1'] and info['W2'] > info['L2'] :
                    player['Win'] += 1
            if info['Loser'] == player_name and info['Best of'] == best_of:
                if info['W1'] > info['L1'] and info['W2'] > info['L2']:
                    player['Loss'] += 1


    elif best_of == "5":
        for info in data:

            if info['Winner'] == player_name and info['Best of'] == best_of:
                if info['W1'] > info['L1'] and info['W2'] > info['L2'] and info['W3'] > info['L3']:
                    player['Win'] += 1


            if info['Loser'] == player_name and info['Best of'] == best_of:
                if info['W1'] > info['L1'] and info['W2'] > info['L2'] and info['W3'] > info['L3']:
                    player['Loss'] += 1

    return player

#Get matches when the player win the first set
def Win_1set(year, player_name, best_of):
    file = open('../JSON_files/ResultATP_'+year+'.json')
    data = json.load(file)
    player= {"Win":0, "Loss":0}

    # Get the player wins and loss

    if best_of == "3":
        for info in data:

            if info['Winner'] == player_name and info['Best of'] == best_of:
                if info['W1'] > info['L1']:
                    player['Win'] += 1

            if info['Loser'] == player_name and info['Best of'] == best_of:
                if info['W1'] > info['L1'] :
                    player['Loss'] += 1

    elif best_of == "5":
        for info in data:

            if info['Winner'] == player_name and info['Best of'] == best_of:
                if info['W1'] > info['L1'] :
                    player['Win'] += 1


            if info['Loser'] == player_name and info['Best of'] == best_of:
                if info['W1'] > info['L1']:
                    player['Loss'] += 1

    return player


#Get matches won in 3 sets
def Win_3sets(year, player_name, best_of):
    file = open('../JSON_files/ResultATP_'+year+'.json')
    data = json.load(file)
    player= {"Win":0, "Loss":0}

    # Get the player wins and loss

    if best_of == "3":
        for info in data:

            if info['Winner'] == player_name and info['Best of'] == best_of:
                if info['W3'] > info['L3']:
                    player['Win'] += 1


            if info['Loser'] == player_name and info['Best of'] == best_of:
                if info['W3'] > info['L3'] :
                    player['Loss'] += 1



    return player


#Get matches won in 3 sets when the player win the first set
def Win_1set_3set(year, player_name, best_of):
    file = open('../JSON_files/ResultATP_'+year+'.json')
    data = json.load(file)
    player= {"Win":0, "Loss":0}

    # Get the player wins and loss

    if best_of == "3":
        for info in data:

            if info['Winner'] == player_name and info['Best of'] == best_of:
                if info['W1'] > info['L1'] and info['W3'] > info['L3']:
                    player['Win'] += 1

            if info['Loser'] == player_name and info['Best of'] == best_of:
                if info['W1'] > info['L1'] and info['W3'] > info['L3']:
                    player['Loss'] += 1


    elif best_of == "5":
        for info in data:

            if info['Winner'] == player_name and info['Best of'] == best_of:
                if info['W1'] > info['L1'] and info['W3'] > info['L3']:
                    player['Win'] += 1


            if info['Loser'] == player_name and info['Best of'] == best_of:
                if info['W1'] > info['L1'] and info['W3'] > info['L3']:
                    player['Loss'] += 1

    return player

#Get matches won in 3 sets when the player loss the first set
def Win_2set_3set(year, player_name, best_of):
    file = open('../JSON_files/ResultATP_'+year+'.json')
    data = json.load(file)
    player= {"Win":0, "Loss":0}

    # Get the player wins and loss

    if best_of == "3":
        for info in data:

            if info['Winner'] == player_name and info['Best of'] == best_of:
                if info['W2'] > info['L2'] and info['W3'] > info['L3']:
                    player['Win'] += 1

            if info['Loser'] == player_name and info['Best of'] == best_of:
                if info['W2'] > info['L2'] and info['W3'] > info['L3']:
                    player['Loss'] += 1


    elif best_of == "5":
        for info in data:

            if info['Winner'] == player_name and info['Best of'] == best_of:
                if info['W2'] > info['L2'] and info['W3'] > info['L3']:
                    player['Win'] += 1


            if info['Loser'] == player_name and info['Best of'] == best_of:
                if info['W2'] > info['L2'] and info['W3'] > info['L3']:
                    player['Loss'] += 1
    return player

#Get matches won in 4 sets
def Matches_win_4sets(year, player_name, best_of):
    file = open('../JSON_files/ResultATP_'+year+'.json')
    data = json.load(file)
    player= {"Win":0, "Loss":0}

    if best_of == "5":
        for info in data:

            if info['Winner'] == player_name and info['Best of'] == best_of:
                if info['W4'] > info['L4'] :
                    player['Win'] += 1


            if info['Loser'] == player_name and info['Best of'] == best_of:
                if info['W4'] > info['L4'] :
                    player['Loss'] += 1
    return player

#Get matches won in 5 sets
def Matches_win_5sets(year, player_name, best_of):
    file = open('../JSON_files/ResultATP_'+year+'.json')
    data = json.load(file)
    player= {"Win":0, "Loss":0}

    if best_of == "5":
        for info in data:

            if info['Winner'] == player_name and info['Best of'] == best_of:
                if info['W5'] > info['L5'] :
                    player['Win'] += 1


            if info['Loser'] == player_name and info['Best of'] == best_of:
                if info['W5'] > info['L5'] :
                    player['Loss'] += 1
    return player


#Consecutive_sets(year, player_name, best_of)
#Win_1set(year, player_name, best_of)
#Win_3sets(year, player_name, best_of)
#Win_1set_3set(year, player_name, best_of)
#Win_2set_3set(year, player_name, best_of)