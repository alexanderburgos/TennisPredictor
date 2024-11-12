from Tennis.Players_Stats import sets

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
    'round': '1st Round'
}


def Sets_Predictor(data):
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

    player1 = {}
    player2 = {}
    average_p1 = 0.0
    average_p2 = 0.0
    prediction = {'p1': [], 'p2': []}
    """
        Match played during the year

    """
    player1 = sets.Consecutive_sets(year, player1_name, best_of)
    player2 = sets.Consecutive_sets(year, player2_name, best_of)
    print("Match won in consecutive sets")
    print("{} : {}".format(player1_name, player1))
    print("{} : {}".format(player2_name, player2))

    player1 = sets.Win_1set(year, player1_name, best_of)
    player2 = sets.Win_1set(year, player2_name, best_of)
    print("Match won when the player win the first set")
    print("{} : {}".format(player1_name, player1))
    print("{} : {}".format(player2_name, player2))

    player1 = sets.Win_3sets(year, player1_name, best_of)
    player2 = sets.Win_3sets(year, player2_name, best_of)
    print("Match won in three sets")
    print("{} : {}".format(player1_name, player1))
    print("{} : {}".format(player2_name, player2))

    player1 = sets.Win_1set_3set(year, player1_name, best_of)
    player2 = sets.Win_1set_3set(year, player2_name, best_of)
    print("Match won when the player loss the second set")
    print("{} : {}".format(player1_name, player1))
    print("{} : {}".format(player2_name, player2))

    player1 = sets.Win_2set_3set(year, player1_name, best_of)
    player2 = sets.Win_2set_3set(year, player2_name, best_of)
    print("Match won when the player loss the first set")
    print("{} : {}".format(player1_name, player1))
    print("{} : {}".format(player2_name, player2))

    player1 = sets.Matches_win_4sets(year, player1_name, best_of)
    player2 = sets.Matches_win_4sets(year, player2_name, best_of)
    print("Match won in 4 sets")
    print("{} : {}".format(player1_name, player1))
    print("{} : {}".format(player2_name, player2))

    player1 = sets.Matches_win_5sets(year, player1_name, best_of)
    player2 = sets.Matches_win_5sets(year, player2_name, best_of)
    print("Match won in 5 sets")
    print("{} : {}".format(player1_name, player1))
    print("{} : {}".format(player2_name, player2))

#Sets_Predictor(data)
