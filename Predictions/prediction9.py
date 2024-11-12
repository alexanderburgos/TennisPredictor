from Tennis.Players_Stats import players_titles, h2h, players_activity, rounds

data = {
    'player1_name': 'De Minaur A.',
    'player2_name': 'Kokkinakis T.',
    'surface': 'Hard',
    'tournament_series': 'ATP250',
    'tournament_name': 'Atlanta Open',
    'location': 'Hamburg',
    'year': '2023',
    'best of': '3',
    'round': '1st Round'

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
    best_of = data['best of']
    round = data['round']

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
    Note: In this prediction we compare wins of all time by round



    compare performance of all time by rounds .25
    compare performance of all time by rounds and surface .5

    """

    # compare performance of all time by rounds

    player1 = rounds.Record_rounds_career(player1_name, best_of)
    player2 = rounds.Record_rounds_career(player2_name, best_of)

    # compare victories of all time by round

    if player1[player1_name]['Rounds'][round]['Win'] > player2[player2_name]['Rounds'][round]['Win']:
        prediction['p1'].append(.25)

    elif player1[player1_name]['Rounds'][round]['Win'] < player2[player2_name]['Rounds'][round]['Win']:
        prediction['p2'].append(.25)


    # compare performance of all time by rounds and surface
    player1 = rounds.Record_rounds_surface_career(player1_name, surface,best_of)
    player2 = rounds.Record_rounds_surface_career(player2_name, surface,best_of)

    # compare victories of all time by round and by surface

    if player1[player1_name]['Rounds'][round]['Win'] > player2[player2_name]['Rounds'][round]['Win']:
        prediction['p1'].append(.5)

    elif player1[player1_name]['Rounds'][round]['Win'] < player2[player2_name]['Rounds'][round]['Win']:
        prediction['p2'].append(.5)


    print("Prediction 9: Only wins of all time by round ")
    print(prediction)

    print(player1_name, sum(prediction['p1']))
    print(player2_name, sum(prediction['p2']))

    return prediction

# Match_Predictor(data)
