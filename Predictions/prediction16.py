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
    Note: In this prediction we compare detail and general information, using only average.


    average of all time .25 done
    average of all time on the surface .25 done


    average of the year .5 done
    average of the year on the surface .5 done

    last 10 matches of the year .75 - done

    titles of all time .25 - done
    titles on that surface of all time .25 - done
    titles of all time by series(250,500,M1000,GS) .25 done
    titles of all time by series(250,500,M1000,GS) and surface .25 done

    titles of the year .5 - done
    titles on that surface during the year .5 done
    titles during the year by series(250,500,M1000,GS) .5 done
    titles during the year by series(250,500,M1000,GS) and surface .5 done

    h2h of all time .5 - done
    h2h in the surface .5 - done
    h2h of the year .5 - done
    h2h on the surface in the year .5 - done


    average in the tournament - .25 done
    compare titles in the tournament .25 done
    compare best performance in the tournament .25 done
    performance last year in the tournament .25 done



    compare average of all time by rounds .25
    compare average of all time by rounds and surface .25
    compare average of the year by rounds .25
    compare average of the year by rounds and surface .25
    """


    # compare average of all time
    player1 = players_activity.WL_career_player(player1_name)
    player2 = players_activity.WL_career_player(player2_name)


    try:
        average_p1 = (player1[player1_name]['Win'] / (
                    player1[player1_name]['Win'] + player1[player1_name]['Loss'])) * 100
    except:
        average_p1 = 0.0
    try:
        average_p2 = (player2[player2_name]['Win'] / (
                    player2[player2_name]['Win'] + player2[player2_name]['Loss'])) * 100
    except:
        average_p2 = 0.0

    if average_p1 > average_p2:
        prediction['p1'].append(0.25)
    elif average_p1 < average_p2:
        prediction['p2'].append(0.25)

    # compare average of all time on the surface

    try:
        average_p1 = (player1[player1_name]['W ' + surface] / (
                    player1[player1_name]['W ' + surface] + player1[player1_name]['L ' + surface])) * 100
    except:
        average_p1 = 0.0
    try:
        average_p2 = (player2[player2_name]['W ' + surface] / (
                    player2[player2_name]['W ' + surface] + player2[player2_name]['L ' + surface])) * 100
    except:
        average_p2 = 0.0

    if average_p1 > average_p2:
        prediction['p1'].append(0.25)
    elif average_p1 < average_p2:
        prediction['p2'].append(0.25)


    # compare average of the year
    player1 = players_activity.WL_year_player(player1_name, year)
    player2 = players_activity.WL_year_player(player2_name, year)

    try:
        average_p1 = (player1[player1_name]['Win'] / (
                    player1[player1_name]['Win'] + player1[player1_name]['Loss'])) * 100
    except:
        average_p1 = 0.0
    try:
        average_p2 = (player2[player2_name]['Win'] / (
                    player2[player2_name]['Win'] + player2[player2_name]['Loss'])) * 100
    except:
        average_p2 = 0.0

    if average_p1 > average_p2:
        prediction['p1'].append(0.5)
    elif average_p1 < average_p2:
        prediction['p2'].append(0.5)

    # compare average of the year on the surface
    try:
        average_p1 = (player1[player1_name]['W ' + surface] / (
                    player1[player1_name]['W ' + surface] + player1[player1_name]['L ' + surface])) * 100
    except:
        average_p1 = 0.0
    try:
        average_p2 = (player2[player2_name]['W ' + surface] / (
                    player2[player2_name]['W ' + surface] + player2[player2_name]['L ' + surface])) * 100
    except:
        average_p2 = 0.0

    if average_p1 > average_p2:
        prediction['p1'].append(.5)
    elif average_p1 < average_p2:
        prediction['p2'].append(.5)

    # compare last 10 matches in that year
    player1 = players_activity.Last_10_matches(player1_name, year)
    player2 = players_activity.Last_10_matches(player2_name, year)

    if player1['Win'] > player2['Win']:
        prediction['p1'].append(.75)
    elif player1['Win'] < player2['Win']:
        prediction['p2'].append(.75)

    # compare titles win during career
    player1 = players_titles.Titles_career_player(player1_name)
    player2 = players_titles.Titles_career_player(player2_name)

    if player1[player1_name]['Total titles'] > player2[player2_name]['Total titles']:
        prediction['p1'].append(0.25)
    elif player1[player1_name]['Total titles'] < player2[player2_name]['Total titles']:
        prediction['p2'].append(0.25)

    # compare titles win during career on the surfaces
    if player1[player1_name][surface] > player2[player2_name][surface]:
        prediction['p1'].append(0.25)
    elif player1[player1_name][surface] < player2[player2_name][surface]:
        prediction['p2'].append(0.25)

    # compare titles win during career by series

    if len(player1[player1_name][tournament_series]) > len(player2[player2_name][tournament_series]):
        prediction['p1'].append(0.25)
    elif len(player1[player1_name][tournament_series]) < len(player2[player2_name][tournament_series]):
        prediction['p2'].append(0.25)

    # compare titles won during career by series and surface

    player1 = players_titles.Titles_career_series_surface_player(player1_name, surface)
    player2 = players_titles.Titles_career_series_surface_player(player2_name, surface)

    if len(player1[player1_name][tournament_series]) > len(player2[player2_name][tournament_series]):
        prediction['p1'].append(0.25)
    elif len(player1[player1_name][tournament_series]) < len(player2[player2_name][tournament_series]):
        prediction['p2'].append(0.25)

    # compare titles won during the year

    player1 = players_titles.Titles_year_player(player1_name, year)
    player2 = players_titles.Titles_year_player(player2_name, year)

    if player1[player1_name]['Total titles'] > player2[player2_name]['Total titles']:
        prediction['p1'].append(.5)
    elif player1[player1_name]['Total titles'] < player2[player2_name]['Total titles']:
        prediction['p2'].append(.5)

    # compare titles won on the surface during the year
    if player1[player1_name][surface] > player2[player2_name][surface]:
        prediction['p1'].append(.5)
    elif player1[player1_name][surface] < player2[player2_name][surface]:
        prediction['p2'].append(.5)

    # compare titles by series during the year
    if len(player1[player1_name][tournament_series]) > len(player2[player2_name][tournament_series]):
        prediction['p1'].append(0.5)
    elif len(player1[player1_name][tournament_series]) < len(player2[player2_name][tournament_series]):
        prediction['p2'].append(0.5)

    # compare titles by series and surface during the year

    player1 = players_titles.Titles_year_serie_surface_player(player1_name, year, surface)
    player2 = players_titles.Titles_year_serie_surface_player(player2_name, year, surface)

    if len(player1[player1_name][tournament_series]) > len(player2[player2_name][tournament_series]):
        prediction['p1'].append(.5)
    elif len(player1[player1_name][tournament_series]) < len(player2[player2_name][tournament_series]):
        prediction['p2'].append(.5)

    # compare h2h of all time
    h2h_info = h2h.h2h_all_time(player1_name, player2_name)

    if h2h_info[0] > h2h_info[1]:
        prediction['p1'].append(.5)
    elif h2h_info[0] < h2h_info[1]:
        prediction['p2'].append(.5)

    # compare h2h on the surface of all time
    h2h_info = h2h.h2h_surface(player1_name, player2_name, surface)

    if h2h_info[0] > h2h_info[1]:
        prediction['p1'].append(.5)
    elif h2h_info[0] < h2h_info[1]:
        prediction['p2'].append(.5)

    # compare h2h of the year

    h2h_info = h2h.h2h_year(player1_name, player2_name, year)

    if h2h_info[0] > h2h_info[1]:
        prediction['p1'].append(.5)
    elif h2h_info[0] < h2h_info[1]:
        prediction['p2'].append(.5)

    # compare h2h on the surface in the year
    h2h_info = h2h.h2h_surface_year(player1_name, player2_name, surface, year)

    if h2h_info[0] > h2h_info[1]:
        prediction['p1'].append(.5)
    elif h2h_info[0] < h2h_info[1]:
        prediction['p2'].append(.5)


    # compare average of all time in the tournament
    player1 = players_activity.Record_career_tournament_player(player1_name, tournament_name, location)
    player2 = players_activity.Record_career_tournament_player(player2_name, tournament_name, location)

    try:
        average_p1 = (player1[player1_name]['Win'] / (
                    player1[player1_name]['Win'] + player1[player1_name]['Loss'])) * 100
    except:
        average_p1 = 0.0
    try:
        average_p2 = (player2[player2_name]['Win'] / (
                    player2[player2_name]['Win'] + player2[player2_name]['Loss'])) * 100
    except:
        average_p2 = 0.0

    if average_p1 > average_p2:
        prediction['p1'].append(0.25)
    elif average_p1 < average_p2:
        prediction['p2'].append(0.25)

    # compare titles in that tournament

    player1 = players_activity.Best_performance_tournament_player(player1_name, tournament_name, location)

    player2 = players_activity.Best_performance_tournament_player(player2_name, tournament_name, location)

    if player1[player1_name]['Total Titles'] > player2[player2_name]['Total Titles']:
        prediction['p1'].append(.25)
    elif player1[player1_name]['Total Titles'] < player2[player2_name]['Total Titles']:
        prediction['p2'].append(.25)

    # Best performance in the tournament

    if player1[player1_name]['Total Titles'] == 0 and player2[player2_name]['Total Titles'] == 0:

        if player1[player1_name]['Best Performance']['Win'] > player2[player2_name]['Best Performance']['Win']:
            prediction['p1'].append(.25)
        elif player1[player1_name]['Best Performance']['Win'] < player2[player2_name]['Best Performance']['Win']:
            prediction['p2'].append(.25)

    # performance last year in the tournament

    player1 = players_activity.Last_year_performance_tournament_player(player1_name, tournament_name, year, location)

    player2 = players_activity.Last_year_performance_tournament_player(player2_name, tournament_name, year, location)

    if player1[player1_name]['Performance']['Win'] > player2[player2_name]['Performance']['Win']:
        prediction['p1'].append(.25)
    elif player1[player1_name]['Performance']['Win'] < player2[player2_name]['Performance']['Win']:
        prediction['p2'].append(.25)


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
        prediction['p1'].append(0.25)
    elif average_p1 < average_p2:
        prediction['p2'].append(0.25)

    # compare average during the year by rounds
    player1= rounds.Record_rounds_year(player1_name, year,best_of)
    player2 = rounds.Record_rounds_year(player2_name, year,best_of)

    #average of victories of the year by round
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


    # compare average during the year by rounds and surface

    player1 = rounds.Record_rounds_surface_year(player1_name, year, surface,best_of)
    player2 = rounds.Record_rounds_surface_year(player2_name, year, surface,best_of)

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
        prediction['p1'].append(0.25)
    elif average_p1 < average_p2:
        prediction['p2'].append(0.25)


#------------------------------------------------------------------------------------------------------------------
    print("Prediction 11: Detail and general information, using average and rounds")
    print(prediction)

    print(player1_name, sum(prediction['p1']))
    print(player2_name, sum(prediction['p2']))

    return prediction

# Match_Predictor(data)
