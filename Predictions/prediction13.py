from Tennis.Players_Stats import players_titles, h2h, players_activity

data = {
    'player1_name': 'De Minaur A.',
    'player2_name': 'Kokkinakis T.',
    'surface': 'Hard',
    'tournament_series': 'ATP250',
    'tournament_name': 'Atlanta Open',
    'location': 'Hamburg',
    'year': '2023'

}


def Match_Predictor(data):
    player1_name = data['player1_name']
    player2_name = data['player2_name']
    surface = data['surface']
    # Serie's tornaments: ATP250 - ATP500 - Masters 1000 - Grand Slam
    tournament_series = data['tournament_series']
    tournament_name = data['tournament_name']
    year = data['year']
    location = data['location']

    player1 = {}
    player2 = {}
    average_p1 = 0.0
    average_p2 = 0.0
    prediction = {'p1': [], 'p2': []}
    """

    :param player1_name:
    :param player2_name:
    player1 = {}
    player2 = {}
    prediction = {p1:[],p2:[]}
    :return: winner
    """

    """
    Note: In this prediction we compare titles wins of all time
    
    titles of all time .25 - done
    titles on that surface of all time .5 - done
    titles of all time by series(250,500,M1000,GS) .25 done
    titles of all time by series(250,500,M1000,GS) and surface .5 done

    """



    # compare titles win during career
    player1 = players_titles.Titles_career_player(player1_name)
    player2 = players_titles.Titles_career_player(player2_name)

    if player1[player1_name]['Total titles'] > player2[player2_name]['Total titles']:
        prediction['p1'].append(0.25)
    elif player1[player1_name]['Total titles'] < player2[player2_name]['Total titles']:
        prediction['p2'].append(0.25)



    # compare titles win during career on the surfaces
    if player1[player1_name][surface] > player2[player2_name][surface]:
        prediction['p1'].append(0.5)
    elif player1[player1_name][surface] < player2[player2_name][surface]:
        prediction['p2'].append(0.5)

    # compare titles win during career by series

    if len(player1[player1_name][tournament_series]) > len(player2[player2_name][tournament_series]):
        prediction['p1'].append(0.25)
    elif len(player1[player1_name][tournament_series]) < len(player2[player2_name][tournament_series]):
        prediction['p2'].append(0.25)

    # compare titles won during career by series and surface

    player1 = players_titles.Titles_career_series_surface_player(player1_name, surface)
    player2 = players_titles.Titles_career_series_surface_player(player2_name, surface)

    if len(player1[player1_name][tournament_series]) > len(player2[player2_name][tournament_series]):
        prediction['p1'].append(0.5)
    elif len(player1[player1_name][tournament_series]) < len(player2[player2_name][tournament_series]):
        prediction['p2'].append(0.5)


    print("Prediction 13: Titles of all time")
    print(prediction)

    print(player1_name, sum(prediction['p1']))
    print(player2_name, sum(prediction['p2']))

    return prediction

# Match_Predictor(data)
