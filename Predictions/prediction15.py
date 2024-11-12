from Tennis.Players_Stats import players_titles, h2h, players_activity, rounds

data = {
    'player1_name': 'De Minaur A.',
    'player2_name': 'Kokkinakis T.',
    'surface': 'Hard',
    'tournament_series': 'ATP250',
    'tournament_name': 'Atlanta Open',
    'location': 'Hamburg',
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
    # '1st Round', '2nd Round', '3rd Round', '4th Round', 'Quarterfinals', 'Semifinals', 'The Final'
    round = data['round']
    last_year = int(year) - 1
    last_year = str(last_year)
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
    Note: In this prediction we compare detail and general information.

    wins of all year .25 done
    winning in that surface last year .5 - done


    winning of the year .25 - done
    winning of the year on the surface .75 done

    total matches of last year played on the surface .25
    total matches of the year played on the surface .5


    titles of last year .25 - done
    titles on that surface of last year .25 - done
    titles of lastyear by series(250,500,M1000,GS) .25 done
    titles of last year by series(250,500,M1000,GS) and surface .5 done

    titles of the year .25 - done
    titles on that surface during the year .5 done
    titles during the year by series(250,500,M1000,GS) .25 done
    titles during the year by series(250,500,M1000,GS) and surface .75 done

    h2h of last year .5 - done
    h2h in the surface last year .5 - done
    h2h of the year 1.25 - done
    h2h on the surface in the year 1.5 - done


    performance last year in the tournament .25 done

    compare performance of last year by rounds in best of 3 or 5 sets - .25
    compare performance of last year by rounds and surface in best of 3 or 5 sets - .25

    compare performance of the year by rounds in best of 3 or 5 sets - .25
    compare performance of the year by rounds and surface in best of 3 or 5 sets - .5
    """

    # compare wins of the last year
    player1 = players_activity.WL_year_player(player1_name, last_year)
    player2 = players_activity.WL_year_player(player2_name, last_year)

    if player1[player1_name]['Win'] > player2[player2_name]['Win']:
        prediction['p1'].append(.25)
    elif player1[player1_name]['Win'] < player2[player2_name]['Win']:
        prediction['p2'].append(.25)

    # compare wins of the last year on the surface

    if player1[player1_name]['W ' + surface] > player2[player2_name]['W ' + surface]:
        prediction['p1'].append(.75)
    elif player1[player1_name]['W ' + surface] < player2[player2_name]['W ' + surface]:
        prediction['p2'].append(.75)

    # compare wins of the year
    player1 = players_activity.WL_year_player(player1_name, year)
    player2 = players_activity.WL_year_player(player2_name, year)

    if player1[player1_name]['Win'] > player2[player2_name]['Win']:
        prediction['p1'].append(.25)
    elif player1[player1_name]['Win'] < player2[player2_name]['Win']:
        prediction['p2'].append(.25)

    # compare wins of the year on the surface

    if player1[player1_name]['W ' + surface] > player2[player2_name]['W ' + surface]:
        prediction['p1'].append(.75)
    elif player1[player1_name]['W ' + surface] < player2[player2_name]['W ' + surface]:
        prediction['p2'].append(.75)

    # compare total matches played during the last year
    player1 = players_activity.WL_year_player(player1_name, last_year)
    player2 = players_activity.WL_year_player(player2_name, last_year)
    if int(player1[player1_name]['Win']) + int(player1[player1_name]['Loss']) > int(player2[player2_name]['Win']) + int(
            player2[player2_name]['Loss']):
        prediction['p1'].append(0.5)
    elif int(player1[player1_name]['Win']) + int(player1[player1_name]['Loss']) < int(
            player2[player2_name]['Win']) + int(player2[player2_name]['Loss']):
        prediction['p2'].append(0.5)

    # compare total matches played during the year
    player1 = players_activity.WL_year_player(player1_name, year)
    player2 = players_activity.WL_year_player(player2_name, year)
    if int(player1[player1_name]['Win']) + int(player1[player1_name]['Loss']) > int(player2[player2_name]['Win']) + int(
            player2[player2_name]['Loss']):
        prediction['p1'].append(0.5)
    elif int(player1[player1_name]['Win']) + int(player1[player1_name]['Loss']) < int(
            player2[player2_name]['Win']) + int(player2[player2_name]['Loss']):
        prediction['p2'].append(0.5)

    # compare titles won during the last year

    player1 = players_titles.Titles_year_player(player1_name, last_year)
    player2 = players_titles.Titles_year_player(player2_name, last_year)

    if player1[player1_name]['Total titles'] > player2[player2_name]['Total titles']:
        prediction['p1'].append(.25)
    elif player1[player1_name]['Total titles'] < player2[player2_name]['Total titles']:
        prediction['p2'].append(.25)

    # compare titles won on the surface during the last year
    if player1[player1_name][surface] > player2[player2_name][surface]:
        prediction['p1'].append(.5)
    elif player1[player1_name][surface] < player2[player2_name][surface]:
        prediction['p2'].append(.5)

    # compare titles by series during the last year
    try:
        if len(player1[player1_name][tournament_series]) > len(player2[player2_name][tournament_series]):
            prediction['p1'].append(0.25)
        elif len(player1[player1_name][tournament_series]) < len(player2[player2_name][tournament_series]):
            prediction['p2'].append(0.25)
    except:
        prediction['p1'].append(0)
        prediction['p2'].append(0)

    # compare titles by series and surface during the last year

    player1 = players_titles.Titles_year_serie_surface_player(player1_name, last_year, surface)
    player2 = players_titles.Titles_year_serie_surface_player(player2_name, last_year, surface)

    try:
        if len(player1[player1_name][tournament_series]) > len(player2[player2_name][tournament_series]):
            prediction['p1'].append(.75)
        elif len(player1[player1_name][tournament_series]) < len(player2[player2_name][tournament_series]):
            prediction['p2'].append(.75)
    except:
        prediction['p1'].append(0)
        prediction['p2'].append(0)

    # compare titles won during the year

    player1 = players_titles.Titles_year_player(player1_name, year)
    player2 = players_titles.Titles_year_player(player2_name, year)

    if player1[player1_name]['Total titles'] > player2[player2_name]['Total titles']:
        prediction['p1'].append(.25)
    elif player1[player1_name]['Total titles'] < player2[player2_name]['Total titles']:
        prediction['p2'].append(.25)

    # compare titles won on the surface during the year
    if player1[player1_name][surface] > player2[player2_name][surface]:
        prediction['p1'].append(.5)
    elif player1[player1_name][surface] < player2[player2_name][surface]:
        prediction['p2'].append(.5)

    # compare titles by series during the year
    try:
        if len(player1[player1_name][tournament_series]) > len(player2[player2_name][tournament_series]):
            prediction['p1'].append(0.25)
        elif len(player1[player1_name][tournament_series]) < len(player2[player2_name][tournament_series]):
            prediction['p2'].append(0.25)
    except:
        prediction['p1'].append(0)
        prediction['p2'].append(0)

    # compare titles by series and surface during the year

    player1 = players_titles.Titles_year_serie_surface_player(player1_name, year, surface)
    player2 = players_titles.Titles_year_serie_surface_player(player2_name, year, surface)

    try:

        if len(player1[player1_name][tournament_series]) > len(player2[player2_name][tournament_series]):
            prediction['p1'].append(.75)
        elif len(player1[player1_name][tournament_series]) < len(player2[player2_name][tournament_series]):
            prediction['p2'].append(.75)
    except:
        prediction['p1'].append(0)
        prediction['p2'].append(0)


    # compare h2h of the last year

    h2h_info = h2h.h2h_year(player1_name, player2_name, last_year)

    if h2h_info[0] > h2h_info[1]:
        prediction['p1'].append(1.25)
    elif h2h_info[0] < h2h_info[1]:
        prediction['p2'].append(1.25)

    # compare h2h on the surface in the last year
    h2h_info = h2h.h2h_surface_year(player1_name, player2_name, surface, last_year)

    if h2h_info[0] > h2h_info[1]:
        prediction['p1'].append(1.5)
    elif h2h_info[0] < h2h_info[1]:
        prediction['p2'].append(1.5)

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


    # performance last year in the tournament

    player1 = players_activity.Last_year_performance_tournament_player(player1_name, tournament_name, year, location)

    player2 = players_activity.Last_year_performance_tournament_player(player2_name, tournament_name, year, location)

    if player1[player1_name]['Performance']['Win'] > player2[player2_name]['Performance']['Win']:
        prediction['p1'].append(.25)
    elif player1[player1_name]['Performance']['Win'] < player2[player2_name]['Performance']['Win']:
        prediction['p2'].append(.25)

        # compare performance during the last year by rounds

        player1 = rounds.Record_rounds_year(player1_name, last_year, best_of)
        player2 = rounds.Record_rounds_year(player2_name, last_year, best_of)


        if player1[player1_name]['Rounds'][round]['Win'] > player2[player2_name]['Rounds'][round]['Win']:
            prediction['p1'].append(.25)

        elif player1[player1_name]['Rounds'][round]['Win'] < player2[player2_name]['Rounds'][round]['Win']:
            prediction['p2'].append(.25)

        # compare performance during the last year by rounds and surface

        player1 = rounds.Record_rounds_surface_year(player1_name, last_year, surface, best_of)
        player2 = rounds.Record_rounds_surface_year(player2_name, last_year, surface, best_of)


        if player1[player1_name]['Rounds'][round]['Win'] > player2[player2_name]['Rounds'][round]['Win']:
            prediction['p1'].append(.5)

        elif player1[player1_name]['Rounds'][round]['Win'] < player2[player2_name]['Rounds'][round]['Win']:
            prediction['p2'].append(.5)

        # compare performance during the year by rounds

        player1 = rounds.Record_rounds_year(player1_name, year, best_of)
        player2 = rounds.Record_rounds_year(player2_name, year, best_of)


        if player1[player1_name]['Rounds'][round]['Win'] > player2[player2_name]['Rounds'][round]['Win']:
            prediction['p1'].append(.25)

        elif player1[player1_name]['Rounds'][round]['Win'] < player2[player2_name]['Rounds'][round]['Win']:
            prediction['p2'].append(.25)

        # compare performance during the year by rounds and surface

        player1 = rounds.Record_rounds_surface_year(player1_name, year, surface, best_of)
        player2 = rounds.Record_rounds_surface_year(player2_name, year, surface, best_of)


        if player1[player1_name]['Rounds'][round]['Win'] > player2[player2_name]['Rounds'][round]['Win']:
            prediction['p1'].append(.5)

        elif player1[player1_name]['Rounds'][round]['Win'] < player2[player2_name]['Rounds'][round]['Win']:
            prediction['p2'].append(.5)

    print("Prediction 15: Detail and general information from last year and the current year")
    print(prediction)

    print(player1_name, sum(prediction['p1']))
    print(player2_name, sum(prediction['p2']))

    return prediction

# Match_Predictor(data)
