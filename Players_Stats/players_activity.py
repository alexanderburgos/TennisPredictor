import json

player_name='Wolf J.J.'
year='2024'
tournament_name='European Open'
location = 'Hamburg'

def WL_year(year):
    file = open('../JSON_files/ResultATP_'+year+'.json')
    data = json.load(file)
    players= {}

    # Get the players wins and loss

    for info in data:
        if info['Winner'] not in players:
            players[info['Winner']] = {"Win":0,"Loss":0, "W Clay": 0, "L Clay": 0, "W Grass": 0, "L Grass": 0, "W Hard": 0, "L Hard": 0}
        if info['Loser'] not in players:
            players[info['Loser']] = {"Win":0,"Loss":0, "W Clay": 0, "L Clay": 0, "W Grass": 0, "L Grass": 0, "W Hard": 0, "L Hard": 0}

    for info in data:
        if info['Winner'] in players:
            players[info['Winner']]['Win'] += 1
            # count the winnings by surface
            if info['Surface'] == 'Hard':
                players[info['Winner']]['W Hard'] += 1
            elif info['Surface'] == 'Grass':
                players[info['Winner']]['W Grass'] += 1
            elif info['Surface'] == 'Clay':
                players[info['Winner']]['W Clay'] += 1

        if info['Loser'] in players:
            players[info['Loser']]['Loss'] += 1
            # count the losses by surface
            if info['Surface'] == 'Hard':
                players[info['Loser']]['L Hard'] += 1
            elif info['Surface'] == 'Grass':
                players[info['Loser']]['L Grass'] += 1
            elif info['Surface'] == 'Clay':
                players[info['Loser']]['L Clay'] += 1


    sorted_titles = sorted(players.items(), key = lambda x:x[1]['Win'], reverse=True)
    players=dict(sorted_titles)
    print(players)

def WL_career():

    players = {}
    #loop to take data from every year since 2000 until now
    for year in range(2000,2024,1):
        year=str(year)
        file = open('../JSON_files/ResultATP_' + year + '.json')
        data = json.load(file)

        # Get the players wins and loss of all time and in each surface

        for info in data:

            if info['Winner'] not in players:
                players[info['Winner']] = {"Win": 0, "Loss": 0, "W Clay": 0, "L Clay": 0, "W Grass": 0, "L Grass": 0, "W Hard": 0, "L Hard": 0, "W Carpet":0, "L Carpet":0}
            if info['Loser'] not in players:
                players[info['Loser']] = {"Win": 0, "Loss": 0, "W Clay": 0, "L Clay": 0, "W Grass": 0, "L Grass": 0, "W Hard": 0, "L Hard": 0, "W Carpet":0, "L Carpet":0}

        for info in data:
            if info['Winner'] in players:
                players[info['Winner']]['Win'] += 1
                #count the winnings by surface
                if info['Surface'] == 'Hard':
                    players[info['Winner']]['W Hard'] += 1
                elif info['Surface'] == 'Grass':
                    players[info['Winner']]['W Grass'] += 1
                elif info['Surface'] == 'Clay':
                    players[info['Winner']]['W Clay'] += 1
                elif info['Surface'] == 'Carpet':
                    players[info['Winner']]['W Carpet'] += 1
            if info['Loser'] in players:
                players[info['Loser']]['Loss'] += 1
                #count the losses by surface
                if info['Surface'] == 'Hard':
                    players[info['Loser']]['L Hard'] += 1
                elif info['Surface'] == 'Grass':
                    players[info['Loser']]['L Grass'] += 1
                elif info['Surface'] == 'Clay':
                    players[info['Loser']]['L Clay'] += 1
                elif info['Surface'] == 'Carpet':
                    players[info['Loser']]['L Carpet'] += 1

    sorted_titles = sorted(players.items(), key=lambda x: x[1]['Win'], reverse=True)
    players = dict(sorted_titles)
    print(players)

#last 10 matches in that year
def Last_10_matches(player_name, year):
    file = open('../JSON_files/ResultATP_'+year+'.json')
    data = json.load(file)
    player = {'last_10':[], 'Win':0, 'Loss':0}

    # Get the players wins and loss of the last 10 matches



    for info in data:
        if info['Winner'] in player_name:
            player['last_10'].append(info)
        if info['Loser'] in player_name:
            player['last_10'].append(info)


    try:
        for i in player['last_10'][-10:]:
            if i['Winner'] == player_name:
                player['Win'] += 1
            if i['Loser'] == player_name:
                player['Loss'] += 1

    except:
        pass


    return player

def WL_career_player(player_name):
    player={}
    player[player_name] = {"Win": 0, "Loss": 0, "W Clay": 0, "L Clay": 0, "W Grass": 0, "L Grass": 0, "W Hard": 0, "L Hard": 0, "W Carpet":0, "L Carpet":0}
    #loop to take data from every year since 2000 until now
    for year in range(2000,2024,1):
        year=str(year)
        file = open('../JSON_files/ResultATP_' + year + '.json')
        data = json.load(file)

        # Get the player wins and loss of all time and in each surface


        for info in data:
            if info['Winner'] in player:
                player[info['Winner']]['Win'] += 1
                #count the winnings by surface
                if info['Surface'] == 'Hard':
                    player[info['Winner']]['W Hard'] += 1
                elif info['Surface'] == 'Grass':
                    player[info['Winner']]['W Grass'] += 1
                elif info['Surface'] == 'Clay':
                    player[info['Winner']]['W Clay'] += 1
                elif info['Surface'] == 'Carpet':
                    player[info['Winner']]['W Carpet'] += 1
            if info['Loser'] in player:
                player[info['Loser']]['Loss'] += 1
                #count the losses by surface
                if info['Surface'] == 'Hard':
                    player[info['Loser']]['L Hard'] += 1
                elif info['Surface'] == 'Grass':
                    player[info['Loser']]['L Grass'] += 1
                elif info['Surface'] == 'Clay':
                    player[info['Loser']]['L Clay'] += 1
                elif info['Surface'] == 'Carpet':
                    player[info['Loser']]['L Carpet'] += 1

    #sorted_titles = sorted(players.items(), key=lambda x: x[1]['Win'], reverse=True)
    #players = dict(sorted_titles)
    return player
def WL_year_player(player_name, year):
    player={}
    player[player_name] = {"Win": 0, "Loss": 0, "W Clay": 0, "L Clay": 0, "W Grass": 0, "L Grass": 0, "W Hard": 0, "L Hard": 0, "W Carpet":0, "L Carpet":0}
    #loop to take data from every year since 2000 until now

    file = open('../JSON_files/ResultATP_' + year + '.json')
    data = json.load(file)

    # Get the player wins and loss of all time and in each surface


    for info in data:
        if info['Winner'] in player:
            player[info['Winner']]['Win'] += 1
            #count the winnings by surface
            if info['Surface'] == 'Hard':
                player[info['Winner']]['W Hard'] += 1
            elif info['Surface'] == 'Grass':
                player[info['Winner']]['W Grass'] += 1
            elif info['Surface'] == 'Clay':
                player[info['Winner']]['W Clay'] += 1
            elif info['Surface'] == 'Carpet':
                player[info['Winner']]['W Carpet'] += 1
        if info['Loser'] in player:
            player[info['Loser']]['Loss'] += 1
            #count the losses by surface
            if info['Surface'] == 'Hard':
                player[info['Loser']]['L Hard'] += 1
            elif info['Surface'] == 'Grass':
                player[info['Loser']]['L Grass'] += 1
            elif info['Surface'] == 'Clay':
                player[info['Loser']]['L Clay'] += 1
            elif info['Surface'] == 'Carpet':
                player[info['Loser']]['L Carpet'] += 1

    return player

def Record_career_tournament_player(player_name,tournament_name,location):
    player={}
    player[player_name] = {"Win": 0, "Loss": 0}
    #loop to take data from every year since 2000 until now
    for year in range(2000,2024,1):
        year=str(year)
        file = open('../JSON_files/ResultATP_' + year + '.json')
        data = json.load(file)

        # Get the player wins and loss of all time and in each surface


        for info in data:

            if info['Tournament'] == tournament_name and info['Location'] == location:
                if info['Winner'] in player:
                    player[info['Winner']]['Win'] += 1
                if info['Loser'] in player:
                    player[info['Loser']]['Loss'] += 1


    return player


def Best_performance_tournament_player(player_name, tournament_name,location):
    player={}
    player[player_name] = {"Best Performance": {"Year":0,"Round":"","Win":0}, "Total Titles":0}
    #loop to take data from every year since 2000 until now
    for year in range(2000,2024,1):
        year=str(year)
        file = open('../JSON_files/ResultATP_' + year + '.json')
        data = json.load(file)
        wins=0

        # Get the player wins and loss of all time and in each surface

        for info in data:

            if info['Tournament'] == tournament_name and info['Location'] == location:
                if info['Winner'] in player and player[info['Winner']]['Total Titles'] == 0:
                    wins += 1


                if info['Loser'] in player and player[info['Loser']]['Total Titles'] == 0 and player[info['Loser']]['Best Performance']['Win'] < wins:
                    player[info['Loser']]['Best Performance']['Year'] = int(year)
                    player[info['Loser']]['Best Performance']['Round'] = info['Round']
                    player[info['Loser']]['Best Performance']['Win'] = wins



                if info['Winner'] in player and info['Round'] == 'The Final':
                    player[info['Winner']]['Best Performance']['Year'] = int(year)
                    player[info['Winner']]['Best Performance']['Round'] = 'Champion'
                    player[info['Winner']]['Total Titles'] += 1
                    player[info['Winner']]['Best Performance']['Win'] = wins
    return player




def Last_year_performance_tournament_player(player_name, tournament_name, year,location):
    player={}
    player[player_name] = {"Performance": {"Year":'',"Round":"","Win":0}}
    year=int(year)
    year -= 1
    year=str(year)
    file = open('../JSON_files/ResultATP_' + year + '.json')
    data = json.load(file)
    wins=0

    # Get the player wins and loss of all time and in each surface

    for info in data:

        if info['Tournament'] == tournament_name and info['Location'] == location:
            if info['Winner'] in player:
                wins += 1

            if info['Loser'] in player:
                player[info['Loser']]['Performance']['Year'] = year
                player[info['Loser']]['Performance']['Round'] = info['Round']
                player[info['Loser']]['Performance']['Win'] = wins



            if info['Winner'] in player and info['Round'] == 'The Final':
                player[info['Winner']]['Performance']['Year'] = year
                player[info['Winner']]['Performance']['Round'] = 'Champion'
                player[info['Winner']]['Performance']['Win'] = wins
    return player
#Last_10_matches(player_name, year)
#WL_year(year)
#WL_career()
#WL_career_player(player_name)
#WL_year_player(player_name, year)
#Record_career_tournament_player(player_name,tournament_name, location)
#Best_performance_tournament_player(player_name, tournament_name, location)
#Last_year_performance_tournament_player(player_name, tournament_name, year, location)