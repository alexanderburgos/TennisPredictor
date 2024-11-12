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
    Note: In this prediction we compare total matches of the year

    """
    player1 = players_activity.WL_year_player(player1_name, year)
    player2 = players_activity.WL_year_player(player2_name, year)

    # compare total matches played during the year
    if int(player1[player1_name]['Win']) + int(player1[player1_name]['Loss']) > int(player2[player2_name]['Win']) + int(
            player2[player2_name]['Loss']):
        prediction['p1'].append(0.25)
    elif int(player1[player1_name]['Win']) + int(player1[player1_name]['Loss']) < int(
            player2[player2_name]['Win']) + int(player2[player2_name]['Loss']):
        prediction['p2'].append(0.25)


    # compare total matches played during the year on the surface
    if int(player1[player1_name]['W '+ surface]) + int(player1[player1_name]['L '+surface]) > int(player2[player2_name]['W '+ surface]) + \
            int(player2[player2_name]['L '+surface]):
        prediction['p1'].append(0.5)
    elif int(player1[player1_name]['W '+ surface]) + int(player1[player1_name]['L '+surface]) < int(player2[player2_name]['W '+ surface]) + \
            int(player2[player2_name]['L '+surface]):
        prediction['p2'].append(0.5)

    print("Prediction 12: Matches played during the year")
    print(prediction)

    print(player1_name, sum(prediction['p1']))
    print(player2_name, sum(prediction['p2']))

    return prediction

# Match_Predictor(data)
