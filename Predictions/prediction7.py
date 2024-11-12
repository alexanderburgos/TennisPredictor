from Tennis.Players_Stats import players_titles, h2h, players_activity, rounds

data = {
    'player1_name': 'De Minaur A.',
    'player2_name': 'Kokkinakis T.',
    'surface': 'Hard',
    # Serie's tornaments: ATP250 - ATP500 - Masters 1000 - Grand Slam
    'tournament_series': 'ATP250',
    'tournament_name': 'Atlanta Open',
    'location': 'Hamburg',
    'year': '2023',
    'best of': '3',
    # '1st Round', '2nd Round', '3rd Round', '4th Round', 'Quarterfinals', 'Semifinals', 'The Final'
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
    Note: In this prediction we compare average round of all time

    compare average of all time by rounds .25
    compare average of all time by rounds and surface .5
    """


    # compare victories of all time by round
    player1= rounds.Record_rounds_career(player1_name, best_of)
    player2 = rounds.Record_rounds_career(player2_name, best_of)

    # average of victories of all time by round
    try:
        average_p1 = (player1[player1_name]['Rounds'][round]['Win'] / (
                player1[player1_name]['Rounds'][round]['Win'] + player1[player1_name]['Rounds'][round]['Loss'])) * 100
    except:
        average_p1 = 0.0
    try:
        average_p2 = (player2[player2_name]['Rounds'][round]['Win'] / (
                player2[player2_name]['Rounds'][round]['Win'] + player2[player2_name]['Rounds'][round]['Loss'])) * 100
    except:
        average_p2 = 0.0

    if average_p1 > average_p2:
        prediction['p1'].append(0.25)
    elif average_p1 < average_p2:
        prediction['p2'].append(0.25)


    # compare average of all time by rounds and surface
    player1 = rounds.Record_rounds_surface_career(player1_name, surface,best_of)
    player2 = rounds.Record_rounds_surface_career(player2_name, surface,best_of)

    #average of victories of all time by round and surface
    try:
        average_p1 = (player1[player1_name]['Rounds'][round]['Win'] / (
                player1[player1_name]['Rounds'][round]['Win'] + player1[player1_name]['Rounds'][round]['Loss'])) * 100
    except:
        average_p1 = 0.0
    try:
        average_p2 = (player2[player2_name]['Rounds'][round]['Win'] / (
                player2[player2_name]['Rounds'][round]['Win'] + player2[player2_name]['Rounds'][round]['Loss'])) * 100
    except:
        average_p2 = 0.0

    if average_p1 > average_p2:
        prediction['p1'].append(0.5)
    elif average_p1 < average_p2:
        prediction['p2'].append(0.5)


    print("Prediction 7: Only average round of all time by round")
    print(prediction)

    print(player1_name, sum(prediction['p1']))
    print(player2_name, sum(prediction['p2']))

    return prediction


# Match_Predictor(data)
