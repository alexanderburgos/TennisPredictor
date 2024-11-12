from Tennis.Players_Stats import players_titles, h2h, players_activity

data = {
    'player1_name': 'De Minaur A.',
    'player2_name': 'Kokkinakis T.',
    'surface': 'Hard',
    'tournament_series': 'ATP250',
    'tournament_name': 'Atlanta Open',
    'location':'Hamburg',
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
    Note: In this predictor only compare wins of the year
    
    winning  of all time .25 - done
    winning in that surface of all time .5 - done



   

    """

    # compare wins of all time
    player1 = players_activity.WL_career_player(player1_name)
    player2 = players_activity.WL_career_player(player2_name)

    if player1[player1_name]['Win'] > player2[player2_name]['Win']:
        prediction['p1'].append(0.25)
    elif player1[player1_name]['Win'] < player2[player2_name]['Win']:
        prediction['p2'].append(0.25)

    # compare wins of all time on the surface
    if player1[player1_name]['W ' + surface] > player2[player2_name]['W ' + surface]:
        prediction['p1'].append(0.5)
    elif player1[player1_name]['W ' + surface] < player2[player2_name]['W ' + surface]:
        prediction['p2'].append(0.5)




    print("Prediction 3: Only wins of all time")
    print(prediction)

    print(player1_name, sum(prediction['p1']))
    print(player2_name, sum(prediction['p2']))

    return prediction


#Match_Predictor(data)
