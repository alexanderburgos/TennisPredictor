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
    Note: Compare h2h 


    

    
    h2h of all time 1 - done
    h2h in the surface 1.25 - done
    h2h of the year 1.25 - done
    h2h on the surface in the year 1.5 - done


    """



    # compare h2h of all time
    h2h_info = h2h.h2h_all_time(player1_name, player2_name)

    if h2h_info[0] > h2h_info[1]:
        prediction['p1'].append(1.0)
    elif h2h_info[0] < h2h_info[1]:
        prediction['p2'].append(1.0)

    # compare h2h on the surface of all time
    h2h_info = h2h.h2h_surface(player1_name, player2_name, surface)

    if h2h_info[0] > h2h_info[1]:
        prediction['p1'].append(1.25)
    elif h2h_info[0] < h2h_info[1]:
        prediction['p2'].append(1.25)

    # compare h2h of the year

    h2h_info = h2h.h2h_year(player1_name, player2_name, year)

    if h2h_info[0] > h2h_info[1]:
        prediction['p1'].append(1.25)
    elif h2h_info[0] < h2h_info[1]:
        prediction['p2'].append(1.25)

    # compare h2h on the surface in the year
    h2h_info = h2h.h2h_surface_year(player1_name, player2_name, surface, year)

    if h2h_info[0] > h2h_info[1]:
        prediction['p1'].append(1.5)
    elif h2h_info[0] < h2h_info[1]:
        prediction['p2'].append(1.5)


    print("Prediction 11: Head to head")
    print(prediction)

    print(player1_name, sum(prediction['p1']))
    print(player2_name, sum(prediction['p2']))

    return prediction

# Match_Predictor(data)
