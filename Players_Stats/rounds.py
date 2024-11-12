import json

player_name='Djokovic N.'
year='2023'
surface='Hard'
best_of='5'

#Get the record by rounds of the player during the career in best of 3 sets
def Record_rounds_career(player_name, best_of):
    player={}
    player[player_name] = {'Rounds':{'1st Round':{'Win':0,'Loss':0},
                                     '2nd Round':{'Win':0,'Loss':0},
                                     '3rd Round':{'Win':0,'Loss':0},
                                     '4th Round':{'Win':0,'Loss':0},
                                     'Quarterfinals':{'Win':0,'Loss':0},
                                     'Semifinals':{'Win':0,'Loss':0},
                                     'The Final':{'Win':0,'Loss':0},
                                     'N/A': {'Win':0,'Loss':0}
                                     }}
    #loop to take data from every year since 2000 until now
    for year in range(2000,2024,1):
        year=str(year)
        file = open('../JSON_files/ResultATP_' + year + '.json')
        data = json.load(file)

        # Get the player wins and loss of all time and in each surface

        for info in data:
            if info['Best of'] == best_of:

                #check if the round is added into the dictionary
                if info['Round'] in player[player_name]['Rounds'] and (info['Winner'] == player_name or info['Loser'] == player_name):

                    if info['Round'] in player[player_name]['Rounds'] and info['Winner'] == player_name:
                        player[player_name]['Rounds'][info['Round']]['Win'] += 1

                    if info['Round'] in player[player_name]['Rounds'] and info['Loser'] == player_name:
                        player[player_name]['Rounds'][info['Round']]['Loss'] += 1

                """
                #check if the round is not added into the dictionary
                if info['Round'] not in player[player_name]['Rounds'] and (info['Winner'] == player_name or info['Loser'] == player_name):
                    #create the fields in the dictionary
                    player[player_name]['Rounds'][info['Round']] ={'Win':0,'Loss':0}
                    if info['Round'] in player[player_name]['Rounds'] and info['Winner'] == player_name:
                        player[player_name]['Rounds'][info['Round']]['Win'] += 1
    
                    if info['Round'] in player[player_name]['Rounds'] and info['Loser'] == player_name:
                        player[player_name]['Rounds'][info['Round']]['Loss'] += 1
                """


    #print(player)
    return player

#Get the record by rounds and by surface of the player during the career in best of 3 sets
def Record_rounds_surface_career(player_name, surface, best_of):
    player={}
    player[player_name] = {'Rounds':{'1st Round':{'Win':0,'Loss':0},
                                     '2nd Round':{'Win':0,'Loss':0},
                                     '3rd Round':{'Win':0,'Loss':0},
                                     '4th Round':{'Win':0,'Loss':0},
                                     'Quarterfinals':{'Win':0,'Loss':0},
                                     'Semifinals':{'Win':0,'Loss':0},
                                     'The Final':{'Win':0,'Loss':0},
                                     'N/A': {'Win':0,'Loss':0}
                                     }}

    #loop to take data from every year since 2000 until now
    for year in range(2000,2024,1):
        year=str(year)
        file = open('../JSON_files/ResultATP_' + year + '.json')
        data = json.load(file)

        # Get the player wins and loss of all time and in each surface

        for info in data:
            if info['Best of'] == best_of and info['Surface'] == surface:
                #check if the round is add into the dictionary
                if info['Round'] in player[player_name]['Rounds'] and (info['Winner'] == player_name or info['Loser'] == player_name):

                    if info['Round'] in player[player_name]['Rounds'] and info['Winner'] == player_name:
                        player[player_name]['Rounds'][info['Round']]['Win'] += 1

                    if info['Round'] in player[player_name]['Rounds'] and info['Loser'] == player_name:
                        player[player_name]['Rounds'][info['Round']]['Loss'] += 1

    #print(player)
    return player

#Get the record by rounds of the player during the year in best of 3 sets
def Record_rounds_year(player_name, year, best_of):
    player={}
    player[player_name] = {'Rounds':{'1st Round':{'Win':0,'Loss':0},
                                     '2nd Round':{'Win':0,'Loss':0},
                                     '3rd Round':{'Win':0,'Loss':0},
                                     '4th Round':{'Win':0,'Loss':0},
                                     'Quarterfinals':{'Win':0,'Loss':0},
                                     'Semifinals':{'Win':0,'Loss':0},
                                     'The Final':{'Win':0,'Loss':0},
                                     'N/A': {'Win':0,'Loss':0}
                                     }}

    file = open('../JSON_files/ResultATP_' + year + '.json')
    data = json.load(file)

    # Get the player wins and loss of all time and in each surface

    for info in data:
        if info['Best of'] == best_of:


            #check if the round is add into the dictionary
            if info['Round'] in player[player_name]['Rounds'] and (info['Winner'] == player_name or info['Loser'] == player_name):

                if info['Round'] in player[player_name]['Rounds'] and info['Winner'] == player_name:
                    player[player_name]['Rounds'][info['Round']]['Win'] += 1

                if info['Round'] in player[player_name]['Rounds'] and info['Loser'] == player_name:
                    player[player_name]['Rounds'][info['Round']]['Loss'] += 1





    #print(player)
    return player

#Get the record by rounds  and by surface of the player during the year in best of 3 sets
def Record_rounds_surface_year(player_name, year, surface, best_of):
    player={}
    player[player_name] = {'Rounds':{'1st Round':{'Win':0,'Loss':0},
                                     '2nd Round':{'Win':0,'Loss':0},
                                     '3rd Round':{'Win':0,'Loss':0},
                                     '4th Round':{'Win':0,'Loss':0},
                                     'Quarterfinals':{'Win':0,'Loss':0},
                                     'Semifinals':{'Win':0,'Loss':0},
                                     'The Final':{'Win':0,'Loss':0},
                                     'N/A':{'Win':0,'Loss':0}
                                     }}

    file = open('../JSON_files/ResultATP_' + year + '.json')
    data = json.load(file)

    # Get the player wins and loss of the year and in each surface

    for info in data:
        if info['Best of'] == best_of and info['Surface'] == surface:

            #check if the round is add into the dictionary
            if info['Round'] in player[player_name]['Rounds'] and (info['Winner'] == player_name or info['Loser'] == player_name):

                if info['Round'] in player[player_name]['Rounds'] and info['Winner'] == player_name:
                    player[player_name]['Rounds'][info['Round']]['Win'] += 1

                if info['Round'] in player[player_name]['Rounds'] and info['Loser'] == player_name:
                    player[player_name]['Rounds'][info['Round']]['Loss'] += 1


    #print(player)
    return player



#Record_rounds_career(player_name, best_of)
#Record_rounds_surface_career(player_name, surface,best_of)
#Record_rounds_year(player_name, year,best_of)
#Record_rounds_surface_year(player_name, year, surface,best_of)

