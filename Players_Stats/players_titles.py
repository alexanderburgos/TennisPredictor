import json

year = '2023'
player_name='Norrie C.'
surface='Hard'

# Get the players that have won a titles in the current year and how many titles they won
def Titles_year(year):
    file = open('../JSON_files/ResultATP_'+year+'.json')
    data = json.load(file)
    players={}
    for info in data:
        if info['Winner'] not in players and info['Round'] == 'The Final':
            players[info['Winner']]= {"Total titles":0, "ATP250": [], "ATP500": [], "Masters 1000": [],"Grand Slam": [], "Clay":0, "Grass":0, "Hard":0}
    for info in data:
        if info['Round'] == 'The Final':
            players[info['Winner']]['Total titles'] += 1

            if info['Series'] == "ATP250":
                players[info['Winner']]['ATP250'].append([info['Tournament'], info['Court'],info['Surface']])
            elif info['Series'] == "ATP500":
                players[info['Winner']]['ATP500'].append([info['Tournament'], info['Court'],info['Surface']])
            elif info['Series'] == "Masters 1000":
                players[info['Winner']]['Masters 1000'].append([info['Tournament'], info['Court'],info['Surface']])
            elif info['Series'] == "Grand Slam":
                players[info['Winner']]['Grand Slam'].append([info['Tournament'], info['Court'],info['Surface']])

            if info['Surface'] == 'Hard':
                players[info['Winner']]['Hard'] +=1
            elif info['Surface'] == 'Grass':
                players[info['Winner']]['Grass'] +=1
            elif info['Surface'] == 'Clay':
                players[info['Winner']]['Clay'] +=1

    #sort the dictionary by titles
    sorted_titles = sorted(players.items(), key = lambda x:x[1]['Total titles'], reverse=True)
    players=dict(sorted_titles)
    for player in players:
        print("{} - Total titles = {} - ATP250 = {} - ATP500 = {} - Masters 1000 = {} - Grand Slam = {} - Hard = {} - Clay = {} - Grass = {}".format(player, players[player]['Total titles'], len(players[player]['ATP250']), len(players[player]['ATP500']), len(players[player]['Masters 1000']), len(players[player]['Grand Slam']), players[player]['Hard'], players[player]['Clay'], players[player]['Grass'] ))



def Titles_career():
    players = {}
    for year in range(2000,2024,1):
        year=str(year)
        file = open('../JSON_files/ResultATP_' + year + '.json')
        data = json.load(file)

        for info in data:
            if info['Winner'] not in players and info['Round'] == 'The Final':
                players[info['Winner']] = {"Total titles": 0, "ATP250": [], "ATP500": [], "Masters 1000": [],
                                           "Grand Slam": [], "Clay": 0, "Grass": 0, "Hard": 0, "Carpet":0}

        for info in data:
            if info['Round'] == 'The Final':

                players[info['Winner']]['Total titles'] += 1
                if info['Series'] == "ATP250" or info['Series'] == "International":
                    players[info['Winner']]['ATP250'].append([info['Date'], info['Tournament'], info['Court'], info['Surface']])
                elif info['Series'] == "ATP500" or info['Series'] == "International Gold":
                    players[info['Winner']]['ATP500'].append([info['Date'], info['Tournament'], info['Court'], info['Surface']])
                elif info['Series'] == "Masters 1000" or info['Series'] == "Masters":
                    players[info['Winner']]['Masters 1000'].append([info['Date'], info['Tournament'], info['Court'], info['Surface']])
                elif info['Series'] == "Grand Slam":
                    players[info['Winner']]['Grand Slam'].append([info['Date'], info['Tournament'], info['Court'], info['Surface']])


                if info['Surface'] == 'Hard':
                    players[info['Winner']]['Hard'] += 1
                elif info['Surface'] == 'Grass':
                    players[info['Winner']]['Grass'] += 1
                elif info['Surface'] == 'Clay':
                    players[info['Winner']]['Clay'] += 1
                elif info['Surface'] == 'Carpet':
                    players[info['Winner']]['Carpet'] += 1

    # sort the dictionary by titles

    sorted_titles = sorted(players.items(), key=lambda x: x[1]['Total titles'], reverse=True)
    players = dict(sorted_titles)
    for player in players:
        pass

        print("{} - Total titles = {} - ATP250 = {} - ATP500 = {} - Masters 1000 = {} - Grand Slam = {} - Hard = {} - Clay = {} - Grass = {} - Carpet = {}".format(
        player, players[player]['Total titles'], len(players[player]['ATP250']), len(players[player]['ATP500']),
        len(players[player]['Masters 1000']), len(players[player]['Grand Slam']), players[player]['Hard'],
        players[player]['Clay'], players[player]['Grass'], players[player]['Carpet']))

def Titles_career_player(player_name):
    player = {}
    player[player_name] = {"Total titles": 0, "ATP250": [], "ATP500": [], "Masters 1000": [],
                                           "Grand Slam": [], "Clay": 0, "Grass": 0, "Hard": 0, "Carpet":0}
    for year in range(2000,2024,1):
        year=str(year)
        file = open('../JSON_files/ResultATP_' + year + '.json')
        data = json.load(file)

        for info in data:
            if info['Round'] == 'The Final' and info['Winner'] == player_name:

                player[info['Winner']]['Total titles'] += 1
                if info['Series'] == "ATP250" or info['Series'] == "International":
                    player[info['Winner']]['ATP250'].append([info['Date'], info['Tournament'], info['Court'], info['Surface']])
                elif info['Series'] == "ATP500" or info['Series'] == "International Gold":
                    player[info['Winner']]['ATP500'].append([info['Date'], info['Tournament'], info['Court'], info['Surface']])
                elif info['Series'] == "Masters 1000" or info['Series'] == "Masters":
                    player[info['Winner']]['Masters 1000'].append([info['Date'], info['Tournament'], info['Court'], info['Surface']])
                elif info['Series'] == "Grand Slam":
                    player[info['Winner']]['Grand Slam'].append([info['Date'], info['Tournament'], info['Court'], info['Surface']])


                if info['Surface'] == 'Hard':
                    player[info['Winner']]['Hard'] += 1
                elif info['Surface'] == 'Grass':
                    player[info['Winner']]['Grass'] += 1
                elif info['Surface'] == 'Clay':
                    player[info['Winner']]['Clay'] += 1
                elif info['Surface'] == 'Carpet':
                    player[info['Winner']]['Carpet'] += 1



    return player

def Titles_year_player(player_name, year):
    player = {}
    player[player_name] = {"Total titles": 0, "ATP250": [], "ATP500": [], "Masters 1000": [],
                                           "Grand Slam": [], "Clay": 0, "Grass": 0, "Hard": 0, "Carpet":0}

    file = open('../JSON_files/ResultATP_' + year + '.json')
    data = json.load(file)

    for info in data:
        if info['Round'] == 'The Final' and info['Winner'] == player_name:

            player[info['Winner']]['Total titles'] += 1
            if info['Series'] == "ATP250" or info['Series'] == "International":
                player[info['Winner']]['ATP250'].append([info['Date'], info['Tournament'], info['Court'], info['Surface']])
            elif info['Series'] == "ATP500" or info['Series'] == "International Gold":
                player[info['Winner']]['ATP500'].append([info['Date'], info['Tournament'], info['Court'], info['Surface']])
            elif info['Series'] == "Masters 1000" or info['Series'] == "Masters":
                player[info['Winner']]['Masters 1000'].append([info['Date'], info['Tournament'], info['Court'], info['Surface']])
            elif info['Series'] == "Grand Slam":
                player[info['Winner']]['Grand Slam'].append([info['Date'], info['Tournament'], info['Court'], info['Surface']])


            if info['Surface'] == 'Hard':
                player[info['Winner']]['Hard'] += 1
            elif info['Surface'] == 'Grass':
                player[info['Winner']]['Grass'] += 1
            elif info['Surface'] == 'Clay':
                player[info['Winner']]['Clay'] += 1
            elif info['Surface'] == 'Carpet':
                player[info['Winner']]['Carpet'] += 1


    return player

def Titles_career_series_surface_player(player_name, surface):

    player = {}
    player[player_name] = {"Total titles": 0, "ATP250": [], "ATP500": [], "Masters 1000": [],
                                           "Grand Slam": [], "Clay": 0, "Grass": 0, "Hard": 0, "Carpet":0}

    for year in range(2000,2024,1):
        year=str(year)
        file = open('../JSON_files/ResultATP_' + year + '.json')
        data = json.load(file)

        for info in data:
            if info['Round'] == 'The Final' and info['Winner'] == player_name and info['Surface'] == surface:

                player[info['Winner']]['Total titles'] += 1
                if info['Series'] == "ATP250" or info['Series'] == "International":
                    player[info['Winner']]['ATP250'].append(
                        [info['Date'], info['Tournament'], info['Court'], info['Surface']])
                elif info['Series'] == "ATP500" or info['Series'] == "International Gold":
                    player[info['Winner']]['ATP500'].append(
                        [info['Date'], info['Tournament'], info['Court'], info['Surface']])
                elif info['Series'] == "Masters 1000" or info['Series'] == "Masters":
                    player[info['Winner']]['Masters 1000'].append(
                        [info['Date'], info['Tournament'], info['Court'], info['Surface']])
                elif info['Series'] == "Grand Slam":
                    player[info['Winner']]['Grand Slam'].append(
                        [info['Date'], info['Tournament'], info['Court'], info['Surface']])

                if info['Surface'] == 'Hard':
                    player[info['Winner']]['Hard'] += 1
                elif info['Surface'] == 'Grass':
                    player[info['Winner']]['Grass'] += 1
                elif info['Surface'] == 'Clay':
                    player[info['Winner']]['Clay'] += 1
                elif info['Surface'] == 'Carpet':
                    player[info['Winner']]['Carpet'] += 1

    return player

def Titles_year_serie_surface_player(player_name, year, surface):

    player = {}
    player[player_name] = {"Total titles": 0, "ATP250": [], "ATP500": [], "Masters 1000": [],
                                           "Grand Slam": [], "Clay": 0, "Grass": 0, "Hard": 0, "Carpet":0}

    file = open('../JSON_files/ResultATP_' + year + '.json')
    data = json.load(file)

    for info in data:
        if info['Round'] == 'The Final' and info['Winner'] == player_name and info['Surface'] == surface:

            player[info['Winner']]['Total titles'] += 1
            if info['Series'] == "ATP250" or info['Series'] == "International":
                player[info['Winner']]['ATP250'].append(
                    [info['Date'], info['Tournament'], info['Court'], info['Surface']])
            elif info['Series'] == "ATP500" or info['Series'] == "International Gold":
                player[info['Winner']]['ATP500'].append(
                    [info['Date'], info['Tournament'], info['Court'], info['Surface']])
            elif info['Series'] == "Masters 1000" or info['Series'] == "Masters":
                player[info['Winner']]['Masters 1000'].append(
                    [info['Date'], info['Tournament'], info['Court'], info['Surface']])
            elif info['Series'] == "Grand Slam":
                player[info['Winner']]['Grand Slam'].append(
                    [info['Date'], info['Tournament'], info['Court'], info['Surface']])

            if info['Surface'] == 'Hard':
                player[info['Winner']]['Hard'] += 1
            elif info['Surface'] == 'Grass':
                player[info['Winner']]['Grass'] += 1
            elif info['Surface'] == 'Clay':
                player[info['Winner']]['Clay'] += 1
            elif info['Surface'] == 'Carpet':
                player[info['Winner']]['Carpet'] += 1

    return player


#Titles_year(year)
#Titles_career()
#Titles_career_player(player_name)
#Titles_year_player(player_name, year)
#Titles_career_series_surface_player(player_name, surface)
#Titles_year_serie_surface_player(player_name, year, surface)