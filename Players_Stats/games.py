import json

player_name='Djokovic N.'
year='2023'
tournament_name='European Open'
location = 'Hamburg'
best_of='3'
games_parameter=23.5
surface = 'Hard'


"""
 the best of of 3 sets and 5 sets
    Get how many matches had more games that the game parameter
    Get how many matches had less games that the game parameter
    Get how many matches by surface had more games that the game parameter
    Get how many matches by surface had less games that the game parameter
    Get the average of games in all the matches of the year 
    Get the average of games in all the matches of the year by surface

"""
#Get how many matches had more or less games that the game parameter

def Total_Games(year, player_name, best_of, games_parameter):
    file = open('../JSON_files/ResultATP_'+year+'.json')
    data = json.load(file)
    player= {"games_over":0, "games_under":0}
    games = []

    # Get the games
    if best_of == "3":
        for info in data:

            if (info['Winner'] == player_name or info['Loser'] == player_name) and info['Best of'] == best_of:
                games = [ info['W1'] , info['L1'] , info['W2'] , info['L2'] , info['W3'] , info['L3'] ]

                #delete the empty values
                #-----------------------------------------------------------------------------
                for i in reversed(range(len(games))):
                    if games[i] == '':
                        games.pop(i)
                    else:
                        games[i] = int(games[i])
                #-------------------------------------------------------------------------------

                games = sum(games)
                if games > games_parameter:
                    player['games_over'] +=1
                if games < games_parameter:
                    player['games_under'] +=1


    elif best_of == "5":
        for info in data:

            if (info['Winner'] == player_name or info['Loser'] == player_name) and info['Best of'] == best_of:
                games = [ info['W1'] , info['L1'] , info['W2'] , info['L2'] , info['W3'] , info['L3'], info['W4'] , info['L4'] , info['W5'] , info['L5'] ]

                #delete the empty values
                #-----------------------------------------------------------------------------
                for i in reversed(range(len(games))):
                    if games[i] == '':
                        games.pop(i)
                    else:
                        games[i] = int(games[i])
                #-------------------------------------------------------------------------------

                games = sum(games)
                if games > games_parameter:
                    player['games_over'] +=1
                if games < games_parameter:
                    player['games_under'] +=1

    return player

def Total_Games_surface(year, player_name, best_of, games_parameter, surface):
    file = open('../JSON_files/ResultATP_'+year+'.json')
    data = json.load(file)
    player= {"games_over":0, "games_under":0}
    games = []

    # Get the games
    if best_of == "3":
        for info in data:

            if (info['Winner'] == player_name or info['Loser'] == player_name) and info['Best of'] == best_of and info['Surface'] == surface:
                games = [ info['W1'] , info['L1'] , info['W2'] , info['L2'] , info['W3'] , info['L3'] ]

                #delete the empty values
                #-----------------------------------------------------------------------------
                for i in reversed(range(len(games))):
                    if games[i] == '':
                        games.pop(i)
                    else:
                        games[i] = int(games[i])
                #-------------------------------------------------------------------------------

                games = sum(games)
                if games > games_parameter:
                    player['games_over'] +=1
                if games < games_parameter:
                    player['games_under'] +=1


    elif best_of == "5":
        for info in data:

            if (info['Winner'] == player_name or info['Loser'] == player_name) and info['Best of'] == best_of and info['Surface'] == surface:
                games = [ info['W1'] , info['L1'] , info['W2'] , info['L2'] , info['W3'] , info['L3'], info['W4'] , info['L4'] , info['W5'] , info['L5'] ]

                #delete the empty values
                #-----------------------------------------------------------------------------
                for i in reversed(range(len(games))):
                    if games[i] == '':
                        games.pop(i)
                    else:
                        games[i] = int(games[i])
                #-------------------------------------------------------------------------------

                games = sum(games)
                if games > games_parameter:
                    player['games_over'] +=1
                if games < games_parameter:
                    player['games_under'] +=1
    return player


#Total_Games(year, player_name, best_of, games_parameter)
#Total_Games_surface(year, player_name, best_of, games_parameter, surface)