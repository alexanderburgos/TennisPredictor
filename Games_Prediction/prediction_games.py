from Tennis.Players_Stats import games

data = {
    'player1_name':'De Minaur A.',
    'player2_name':'Djokovic N.',
    'surface':'Hard',
    # Serie's tornaments: ATP250 - ATP500 - Masters 1000 - Grand Slam
    'tournament_series':'Grand Slam',
    'tournament_name':'Us Open',
    'location':'New York',
    'year':'2023',
    'best of':'3',
    # '1st Round', '2nd Round', '3rd Round', '4th Round', 'Quarterfinals', 'Semifinals', 'The Final'
    'round': '1st Round',
    'games_parameter':23
}


def Games_Predictor(data):
    player1_name = data['player1_name']
    player2_name = data['player2_name']
    surface = data['surface']
    # Serie's tornaments: ATP250 - ATP500 - Masters 1000 - Grand Slam
    tournament_series = data['tournament_series']
    tournament_name = data['tournament_name']
    year = data['year']
    location = data['location']
    best_of = data['best of']
    # '1st Round', '2nd Round', '3rd Round', '4th Round', 'Quarterfinals', 'Semifinals', 'The Final'
    round = data['round']
    games_parameter=data['games_parameter']

    player1 = {}
    player2 = {}
    average_p1 = 0.0
    average_p2 = 0.0
    prediction = {'p1': [], 'p2': []}
    """
        Match played during the year

    """

    #Total games by matches during the year
    player1 = games.Total_Games(year, player1_name, best_of, games_parameter)
    player2 = games.Total_Games(year, player2_name, best_of, games_parameter)
    print("Total matches of the year over and under {} games".format(games_parameter))
    print("{} : games over: {} - games under: {}".format(player1_name, player1['games_over'], player1['games_under']))
    print("{} : games over: {} - games under: {}".format(player2_name, player2['games_over'], player2['games_under']))

    #Total games by matches and surface during the year
    player1 = games.Total_Games_surface(year, player1_name, best_of, games_parameter, surface)
    player2 = games.Total_Games_surface(year, player2_name, best_of, games_parameter, surface)
    print("\nTotal matches of the year by surface over and under {} games".format(games_parameter))
    print("{} : games over: {} - games under: {}".format(player1_name, player1['games_over'], player1['games_under']))
    print("{} : games over: {} - games under: {}".format(player2_name, player2['games_over'], player2['games_under']))


#Games_Predictor(data)
