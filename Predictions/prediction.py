from Tennis.Players_Stats import players_titles, h2h, players_activity


data = {
    'player1_name':'De Minaur A.',
'player2_name':'Kokkinakis T.',
'surface':'Hard',
'year':'2024'

}
def Match_Predictor(data):
    player1_name = data['player1_name']
    player2_name = data['player2_name']
    surface = data['surface']
    year = data['year']

    player1={}
    player2={}
    prediction={'p1':[],'p2':[]}
    """

    :param player1_name:
    :param player2_name:
    player1 = {}
    player2 = {}
    prediction = {p1:[],p2:[]}
    :return: winner
    """

    """
    Note: In this prediction we compare basic and general information only. We don't use average in this prediction.
    
    wins of all time .25 done
    winning in that surface of all time .5 - done

    winning of the year .25 - done
    winning of the year on the surface .75 done
    
    titles of all time .25 - done
    titles in that surface of all time .5 - done
    
    title of the year .25- done
    titles of the year on the surfaces .75

    h2h of all time .25 - done
    h2h on the surface .25 - done
    h2h of the year .75 - done
    h2h of the year on the surface 1
    """
    #compare wins of all time
    player1= players_activity.WL_career_player(player1_name)
    player2= players_activity.WL_career_player(player2_name)

    if player1[player1_name]['Win'] > player2[player2_name]['Win']:
        prediction['p1'].append(0.25)
    elif player1[player1_name]['Win'] < player2[player2_name]['Win']:
        prediction['p2'].append(0.25)


    #compare wins of all time in the surface
    if player1[player1_name]['W '+surface] > player2[player2_name]['W '+surface]:
        prediction['p1'].append(0.5)
    elif player1[player1_name]['W '+surface] < player2[player2_name]['W '+surface]:
        prediction['p2'].append(0.5)

    #print("Total matches on the surface",player1[player1_name]['W '+surface])


    #compare wins of the year
    player1= players_activity.WL_year_player(player1_name, year)
    player2= players_activity.WL_year_player(player2_name, year)

    if player1[player1_name]['Win'] > player2[player2_name]['Win']:
        prediction['p1'].append(.25)
    elif player1[player1_name]['Win'] < player2[player2_name]['Win']:
        prediction['p2'].append(.25)

    # compare wins of the year on the surface

    if player1[player1_name]['W ' + surface] > player2[player2_name]['W ' + surface]:
        prediction['p1'].append(.75)
    elif player1[player1_name]['W ' + surface] < player2[player2_name]['W ' + surface]:
        prediction['p2'].append(.75)


    #compare titles win during career
    player1 = players_titles.Titles_career_player(player1_name)
    player2 = players_titles.Titles_career_player(player2_name)

    if player1[player1_name]['Total titles'] > player2[player2_name]['Total titles']:
        prediction['p1'].append(0.25)
    elif player1[player1_name]['Total titles'] < player2[player2_name]['Total titles']:
        prediction['p2'].append(0.25)

    #compare titles win during career on the surfaces
    if player1[player1_name][surface] > player2[player2_name][surface]:
        prediction['p1'].append(0.5)
    elif player1[player1_name][surface] < player2[player2_name][surface]:
        prediction['p2'].append(0.5)


    #compare titles win during the year

    player1 = players_titles.Titles_year_player(player1_name, year)
    player2 = players_titles.Titles_year_player(player2_name, year)

    if player1[player1_name]['Total titles'] > player2[player2_name]['Total titles']:
        prediction['p1'].append(.25)
    elif player1[player1_name]['Total titles'] < player2[player2_name]['Total titles']:
        prediction['p2'].append(.25)

    #compare titles win during the year on the surfaces
    if player1[player1_name][surface] > player2[player2_name][surface]:
        prediction['p1'].append(.75)
    elif player1[player1_name][surface] < player2[player2_name][surface]:
        prediction['p2'].append(.75)


    #compare h2h of all time
    h2h_info = h2h.h2h_all_time(player1_name,player2_name)

    if h2h_info[0] > h2h_info[1]:
        prediction['p1'].append(0.25)
    elif h2h_info[0] < h2h_info[1]:
        prediction['p2'].append(0.25)
    #print("H2H of all time: {}".format(h2h_info))

    # compare h2h on the surface
    h2h_info = h2h.h2h_surface(player1_name, player2_name, surface)

    if h2h_info[0] > h2h_info[1]:
        prediction['p1'].append(.25)
    elif h2h_info[0] < h2h_info[1]:
        prediction['p2'].append(.25)

    # print("H2H on {}: {}".format(surface,h2h_info))

    #compare h2h of the year

    h2h_info = h2h.h2h_year(player1_name,player2_name, year)

    if h2h_info[0] > h2h_info[1]:
        prediction['p1'].append(.75)
    elif h2h_info[0] < h2h_info[1]:
        prediction['p2'].append(.75)
    #print("H2H in {}: {}".format(year,h2h_info))


    # compare h2h on the surface in the year
    h2h_info = h2h.h2h_surface_year(player1_name, player2_name, surface, year)

    if h2h_info[0] > h2h_info[1]:
        prediction['p1'].append(1)
    elif h2h_info[0] < h2h_info[1]:
        prediction['p2'].append(1)


    print("Prediction 1: Basic and general information")
    print(prediction)

    print(player1_name, sum(prediction['p1']))
    print(player2_name, sum(prediction['p2']))

    return prediction

#Match_Predictor(data)
