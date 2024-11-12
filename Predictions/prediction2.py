from Tennis.Players_Stats import players_titles, h2h, players_activity, rounds

data = {
        'player1_name':'De Minaur A.',
    'player2_name':'Kokkinakis T.',
    'surface':'Hard',
    'tournament_series':'ATP250',
    'tournament_name':'Atlanta Open',
    'location':'Hamburg',
    'best of':'3',
    # '1st Round', '2nd Round', '3rd Round', '4th Round', 'Quarterfinals', 'Semifinals', 'The Final'
    'round':'1st Round'
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

    player1 = {}
    player2 = {}
    average_p1=0.0
    average_p2=0.0
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
    
    wins of all time .25 done
    winning in that surface of all time .5 - done

    
    winning of the year .25 - done
    winning of the year on the surface .75 done

    total matches of all time played on the surface .25
    total matches of the year played on the surface .5


    titles of all time .25 - done
    titles on that surface of all time .25 - done
    titles of all time by series(250,500,M1000,GS) .25 done
    titles of all time by series(250,500,M1000,GS) and surface .5 done
    
    titles of the year .25 - done
    titles on that surface during the year .5 done
    titles during the year by series(250,500,M1000,GS) .25 done
    titles during the year by series(250,500,M1000,GS) and surface .75 done

    h2h of all time .5 - done
    h2h in the surface .5 - done
    h2h of the year 1.25 - done
    h2h on the surface in the year 1.5 - done

    
    record in the tournament - .25 done
    compare titles in the tournament .5 done
    compare best performance in the tournament .25 done
    performance last year in the tournament .25 done

    compare performance of all time by rounds in best of 3 or 5 sets - .25
    compare performance of all time by rounds and surface in best of 3 or 5 sets - .25

    compare performance of the year by rounds in best of 3 or 5 sets - .25
    compare performance of the year by rounds and surface in best of 3 or 5 sets - .5
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


    # compare total matches of all times played on that surfaces
    player1 = players_activity.WL_career_player(player1_name)
    player2 = players_activity.WL_career_player(player2_name)
    if int(player1[player1_name]['W ' + surface]) + int(player1[player1_name]['L ' + surface]) > int(
            player2[player2_name]['W ' + surface]) + int(player2[player2_name]['L ' + surface]):
        prediction['p1'].append(0.25)
    elif int(player1[player1_name]['W ' + surface]) + int(player1[player1_name]['L ' + surface]) < int(
            player2[player2_name]['W ' + surface]) + int(player2[player2_name]['L ' + surface]):
        prediction['p2'].append(0.25)

    # compare total matches played during the year
    player1 = players_activity.WL_year_player(player1_name, year)
    player2 = players_activity.WL_year_player(player2_name, year)
    if int(player1[player1_name]['Win']) + int(player1[player1_name]['Loss']) > int(player2[player2_name]['Win']) + int(
            player2[player2_name]['Loss']):
        prediction['p1'].append(0.5)
    elif int(player1[player1_name]['Win']) + int(player1[player1_name]['Loss']) < int(
            player2[player2_name]['Win']) + int(player2[player2_name]['Loss']):
        prediction['p2'].append(0.5)

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

    try:
        if len(player1[player1_name][tournament_series]) > len(player2[player2_name][tournament_series]):
            prediction['p1'].append(0.25)
        elif len(player1[player1_name][tournament_series]) < len(player2[player2_name][tournament_series]):
            prediction['p2'].append(0.25)
    except:
        prediction['p1'].append(0)
        prediction['p2'].append(0)



    #compare titles won during career by series and surface

    player1 = players_titles.Titles_career_series_surface_player(player1_name, surface)
    player2 = players_titles.Titles_career_series_surface_player(player2_name, surface)

    try:

        if len(player1[player1_name][tournament_series]) > len(player2[player2_name][tournament_series]):
            prediction['p1'].append(0.5)
        elif len(player1[player1_name][tournament_series]) < len(player2[player2_name][tournament_series]):
            prediction['p2'].append(0.5)
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


    #compare titles won on the surface during the year
    if player1[player1_name][surface] > player2[player2_name][surface]:
        prediction['p1'].append(.5)
    elif player1[player1_name][surface] < player2[player2_name][surface]:
        prediction['p2'].append(.5)


    #compare titles by series during the year
    try:
        if len(player1[player1_name][tournament_series]) > len(player2[player2_name][tournament_series]):
            prediction['p1'].append(0.25)
        elif len(player1[player1_name][tournament_series]) < len(player2[player2_name][tournament_series]):
            prediction['p2'].append(0.25)
    except:
        prediction['p1'].append(0)
        prediction['p2'].append(0)



    #compare titles by series and surface during the year

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


    # compare h2h of all time
    h2h_info = h2h.h2h_all_time(player1_name, player2_name)

    if h2h_info[0] > h2h_info[1]:
        prediction['p1'].append(.5)
    elif h2h_info[0] < h2h_info[1]:
        prediction['p2'].append(0.5)

    # compare h2h on the surface of all time
    h2h_info = h2h.h2h_surface(player1_name, player2_name, surface)

    if h2h_info[0] > h2h_info[1]:
        prediction['p1'].append(.5)
    elif h2h_info[0] < h2h_info[1]:
        prediction['p2'].append(.5)

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



    #compare record of all time in the tournament
    player1 = players_activity.Record_career_tournament_player(player1_name, tournament_name, location)
    player2 = players_activity.Record_career_tournament_player(player2_name, tournament_name, location)

    if player1[player1_name]['Win'] > player2[player2_name]['Win']:
        prediction['p1'].append(.25)
    elif player1[player1_name]['Win'] < player2[player2_name]['Win']:
        prediction['p2'].append(.25)



    #compare titles in that tournament

    player1 = players_activity.Best_performance_tournament_player(player1_name, tournament_name, location)

    player2 = players_activity.Best_performance_tournament_player(player2_name, tournament_name, location)

    if player1[player1_name]['Total Titles'] > player2[player2_name]['Total Titles']:
        prediction['p1'].append(.5)
    elif player1[player1_name]['Total Titles'] < player2[player2_name]['Total Titles']:
        prediction['p2'].append(.5)


    #Best performance in the tournament

    if player1[player1_name]['Total Titles'] == 0 and  player2[player2_name]['Total Titles'] == 0:

        if player1[player1_name]['Best Performance']['Win'] > player2[player2_name]['Best Performance']['Win']:
            prediction['p1'].append(.25)
        elif player1[player1_name]['Best Performance']['Win'] < player2[player2_name]['Best Performance']['Win']:
            prediction['p2'].append(.25)

    #performance last year in the tournament

    player1 = players_activity.Last_year_performance_tournament_player(player1_name, tournament_name, year, location)

    player2 = players_activity.Last_year_performance_tournament_player(player2_name, tournament_name, year, location)

    if player1[player1_name]['Performance']['Win'] > player2[player2_name]['Performance']['Win']:
        prediction['p1'].append(.25)
    elif player1[player1_name]['Performance']['Win'] < player2[player2_name]['Performance']['Win']:
        prediction['p2'].append(.25)

        # compare performance of all time by rounds

        player1 = rounds.Record_rounds_career(player1_name, best_of)
        player2 = rounds.Record_rounds_career(player2_name, best_of)
        average_p1 = 0.0
        average_p2 = 0.0

        # compare victories of all time by round

        if player1[player1_name]['Rounds'][round]['Win'] > player2[player2_name]['Rounds'][round]['Win']:
            prediction['p1'].append(.25)

        elif player1[player1_name]['Rounds'][round]['Win'] < player2[player2_name]['Rounds'][round]['Win']:
            prediction['p2'].append(.25)


        # -------------------------------------------------------------------------------------
        # compare performance of all time by rounds and surface
        player1 = rounds.Record_rounds_surface_career(player1_name, surface, best_of)
        player2 = rounds.Record_rounds_surface_career(player2_name, surface, best_of)

        # compare victories of all time by round and by surface

        if player1[player1_name]['Rounds'][round]['Win'] > player2[player2_name]['Rounds'][round]['Win']:
            prediction['p1'].append(.25)

        elif player1[player1_name]['Rounds'][round]['Win'] < player2[player2_name]['Rounds'][round]['Win']:
            prediction['p2'].append(.25)


        # compare performance during the year by rounds

        player1 = rounds.Record_rounds_year(player1_name, year, best_of)
        player2 = rounds.Record_rounds_year(player2_name, year, best_of)

        # compare victories of the year by round

        if player1[player1_name]['Rounds'][round]['Win'] > player2[player2_name]['Rounds'][round]['Win']:
            prediction['p1'].append(.25)

        elif player1[player1_name]['Rounds'][round]['Win'] < player2[player2_name]['Rounds'][round]['Win']:
            prediction['p2'].append(.25)


        # compare performance during the year by rounds and surface

        player1 = rounds.Record_rounds_surface_year(player1_name, year, surface, best_of)
        player2 = rounds.Record_rounds_surface_year(player2_name, year, surface, best_of)

        # compare victories of the year by round by surface

        if player1[player1_name]['Rounds'][round]['Win'] > player2[player2_name]['Rounds'][round]['Win']:
            prediction['p1'].append(.5)

        elif player1[player1_name]['Rounds'][round]['Win'] < player2[player2_name]['Rounds'][round]['Win']:
            prediction['p2'].append(.5)


    print("Prediction 2: Detail and general information")
    print(prediction)

    print(player1_name, sum(prediction['p1']))
    print(player2_name, sum(prediction['p2']))

    return prediction

#Match_Predictor(data)
