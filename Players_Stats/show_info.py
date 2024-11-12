import players_titles
import h2h
import players_activity
import rounds

data = {
    'player1_name': 'De Minaur A.',
    'player2_name': 'Kokkinakis T.',
    'surface': 'Hard',
    'tournament_series': 'ATP250',
    'tournament_name': 'Atlanta Open',
    'location': 'Hamburg',
    'year': '2023',
    'best of':'3',
    'round':'1st Round'
}


def Show_Information(data):
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
    wins of all time .25 done
    winning in that surface of all time .5 - done
    total matches on that surface of all time .25 - done
    average of all time .25 done
    average of all time on the surface .25 done
    winning of the year 1 - done
    winning of the year on the surface 1 done
    matches played in that year.25 - done
    last 10 matches of the year 1 - done

    average of the year .5 done
    average of the year on the surface .5 done


    titles of all time .25 - done
    titles on that surface of all time .5 - done
    titles of all time by series(250,500,M1000,GS) .25 done
    titles of all time by series(250,500,M1000,GS) and surface .5 done
    
    titles on that surface during the year 1 done
    titles during the year by series(250,500,M1000,GS) .5 done
    titles during the year by series(250,500,M1000,GS) and surface 1 done
    titles of the year .5- done

    h2h of all time .5 - done
    h2h on the surface of all time

    h2h of the year 1 - done
    h2h in the year on the surface 1 - done

    record in the tournament - .25 done
    average in the tournament .25
    compare titles in the tournament 1 done
    compare best performance in the tournament .5 done
    performance last year in the tournament .25 done



    compare performance(wins and average) of all time by rounds in best of 3 or 5 sets - 
    
    compare performance(wins and average) of all time by rounds and surface in best of 3 or 5 sets -

    
    compare performance(wins and average) of the year by rounds in best of 3 or 5 sets - 
    compare performance(wins and average) of the year by rounds and surface in best of 3 or 5 sets -
    

    """

    print("Show Information")
    # compare wins of all time
    player1 = players_activity.WL_career_player(player1_name)
    player2 = players_activity.WL_career_player(player2_name)

    if player1[player1_name]['Win'] > player2[player2_name]['Win']:
        prediction['p1'].append(0.25)
    elif player1[player1_name]['Win'] < player2[player2_name]['Win']:
        prediction['p2'].append(0.25)

    print('Wins of all time')
    print(player1)
    print(player2)

    # compare wins of all time on the surface
    if player1[player1_name]['W ' + surface] > player2[player2_name]['W ' + surface]:
        prediction['p1'].append(0.5)
    elif player1[player1_name]['W ' + surface] < player2[player2_name]['W ' + surface]:
        prediction['p2'].append(0.5)

    # compare total matches of all times played on that surfaces

    if int(player1[player1_name]['W ' + surface]) + int(player1[player1_name]['L ' + surface]) > int(
            player2[player2_name]['W ' + surface]) + int(player2[player2_name]['L ' + surface]):
        prediction['p1'].append(0.25)
    elif int(player1[player1_name]['W ' + surface]) + int(player1[player1_name]['L ' + surface]) < int(
            player2[player2_name]['W ' + surface]) + int(player2[player2_name]['L ' + surface]):
        prediction['p2'].append(0.25)

    print("Total matches of all time on the surface",
          (int(player1[player1_name]['W ' + surface]) + int(player1[player1_name]['L ' + surface])))
    print("Total matches of all time on the surface",
          (int(player2[player2_name]['W ' + surface]) + int(player2[player2_name]['L ' + surface])))

    # compare average of all time

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

    print("Wins average of all time of {}: {}%".format(player1_name, average_p1))
    print("Wins average of all time of {}: {}%".format(player2_name, average_p2))

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

    print("Wins average of all time of {} on {}: {}%".format(player1_name, surface, average_p1))
    print("Wins average of all time of {} on {}: {}%".format(player2_name, surface, average_p2))

    # compare wins of the year
    player1 = players_activity.WL_year_player(player1_name, year)
    player2 = players_activity.WL_year_player(player2_name, year)

    if player1[player1_name]['Win'] > player2[player2_name]['Win']:
        prediction['p1'].append(1.0)
    elif player1[player1_name]['Win'] < player2[player2_name]['Win']:
        prediction['p2'].append(1.0)

    print("Wins of the year")
    print(player1)
    print(player2)

    # compare wins of the year on the surface

    if player1[player1_name]['W ' + surface] > player2[player2_name]['W ' + surface]:
        prediction['p1'].append(.75)
    elif player1[player1_name]['W ' + surface] < player2[player2_name]['W ' + surface]:
        prediction['p2'].append(.75)

    print("Wins of the year on {}".format(surface))
    print(player1[player1_name]['W ' + surface])
    print(player2[player2_name]['W ' + surface])

    # compare matches played during the year
    if int(player1[player1_name]['Win']) + int(player1[player1_name]['Loss']) > int(player2[player2_name]['Win']) + int(
            player2[player2_name]['Loss']):
        prediction['p1'].append(0.25)
    elif int(player1[player1_name]['Win']) + int(player1[player1_name]['Loss']) < int(
            player2[player2_name]['Win']) + int(player2[player2_name]['Loss']):
        prediction['p2'].append(0.25)

    print("Matches played during the year")
    print(int(player1[player1_name]['Win']) + int(player1[player1_name]['Loss']))
    print(int(player2[player2_name]['Win']) + int(player2[player2_name]['Loss']))

    # compare average of the year

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

    print("Wins average in {} of {}: {}%".format(year, player1_name, average_p1))
    print("Wins average in {} of {}: {}%".format(year, player2_name, average_p2))


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

    print("Wins average in {} of {} on {}: {}%".format(year, player1_name, surface, average_p1))
    print("Wins average in {} of {} on {}: {}%".format(year, player2_name, surface, average_p2))


    # compare last 10 matches in that year
    player1 = players_activity.Last_10_matches(player1_name, year)
    player2 = players_activity.Last_10_matches(player2_name, year)

    if player1['Win'] > player2['Win']:
        prediction['p1'].append(1.0)
    elif player1['Win'] < player2['Win']:
        prediction['p2'].append(1.0)


    print("Last 10 matches of {} : Win = {} Loss = {}".format(player1_name, player1['Win'], player1['Loss']))
    print("Last 10 matches of {} : Win = {} Loss = {}".format(player2_name, player2['Win'], player2['Loss']))



    # compare titles win during career
    player1 = players_titles.Titles_career_player(player1_name)
    player2 = players_titles.Titles_career_player(player2_name)

    if player1[player1_name]['Total titles'] > player2[player2_name]['Total titles']:
        prediction['p1'].append(0.25)
    elif player1[player1_name]['Total titles'] < player2[player2_name]['Total titles']:
        prediction['p2'].append(0.25)


    print('Titles won during career')
    print("{}, titles won during career: {}".format(player1_name, player1[player1_name]['Total titles']))
    print("{}, titles won during career: {}".format(player2_name, player2[player2_name]['Total titles']))

    # compare titles win during career on the surfaces
    if player1[player1_name][surface] > player2[player2_name][surface]:
        prediction['p1'].append(0.5)
    elif player1[player1_name][surface] < player2[player2_name][surface]:
        prediction['p2'].append(0.5)
    print("{}, titles won on {}: {}".format(player1_name, surface, player1[player1_name][surface]))
    print("{}, titles won on {}: {}".format(player2_name, surface, player2[player2_name][surface]))

    # compare titles win during career by series
    try:
        if len(player1[player1_name][tournament_series]) > len(player2[player2_name][tournament_series]):
            prediction['p1'].append(0.25)
        elif len(player1[player1_name][tournament_series]) < len(player2[player2_name][tournament_series]):
            prediction['p2'].append(0.25)
        print("{}, titles {} won during career: {}".format(player1_name, tournament_series,
                                                           len(player1[player1_name][tournament_series])))
        print("{}, titles {} won during career: {}".format(player2_name, tournament_series,
                                                       len(player2[player2_name][tournament_series])))
    except:
        prediction['p1'].append(0)
        prediction['p2'].append(0)
        print("{}, titles {} won during career: N/A".format(player1_name, tournament_series))
        print("{}, titles {} won during career: N/A".format(player2_name, tournament_series))
    # compare titles won during career by series and surface

    player1 = players_titles.Titles_career_series_surface_player(player1_name, surface)
    player2 = players_titles.Titles_career_series_surface_player(player2_name, surface)

    try:
        if len(player1[player1_name][tournament_series]) > len(player2[player2_name][tournament_series]):
            prediction['p1'].append(0.5)
        elif len(player1[player1_name][tournament_series]) < len(player2[player2_name][tournament_series]):
            prediction['p2'].append(0.5)

        print("{}, titles {} won on {} during career: {}".format(player1_name, tournament_series, surface,
                                                                 len(player1[player1_name][tournament_series])))
        print("{}, titles {} won on {} during career: {}".format(player2_name, tournament_series, surface,
                                                                 len(player2[player2_name][tournament_series])))
    except:
        prediction['p1'].append(0)
        prediction['p2'].append(0)
        print("{}, titles {} won during career: N/A".format(player1_name, tournament_series, surface))
        print("{}, titles {} won during career: N/A".format(player2_name, tournament_series, surface))
    # compare titles won during the year

    player1 = players_titles.Titles_year_player(player1_name, year)
    player2 = players_titles.Titles_year_player(player2_name, year)

    if player1[player1_name]['Total titles'] > player2[player2_name]['Total titles']:
        prediction['p1'].append(.5)
    elif player1[player1_name]['Total titles'] < player2[player2_name]['Total titles']:
        prediction['p2'].append(.5)
    print('Titles won during the year')
    print('{} : {}'.format(player1_name, player1[player1_name]['Total titles']))
    print('{} : {}'.format(player2_name, player2[player2_name]['Total titles']))

    # compare titles won on the surface during the year
    if player1[player1_name][surface] > player2[player2_name][surface]:
        prediction['p1'].append(1.0)
    elif player1[player1_name][surface] < player2[player2_name][surface]:
        prediction['p2'].append(1.0)
    print("{}, titles won on {} during the year: {}".format(player1_name, surface, player1[player1_name][surface]))
    print("{}, titles won on {} during the year: {}".format(player2_name, surface, player2[player2_name][surface]))

    # compare titles by series during the year
    try:
        if len(player1[player1_name][tournament_series]) > len(player2[player2_name][tournament_series]):
            prediction['p1'].append(0.5)
        elif len(player1[player1_name][tournament_series]) < len(player2[player2_name][tournament_series]):
            prediction['p2'].append(0.5)
        print("{}, titles {} won during the year: {}".format(player1_name, tournament_series,
                                                             len(player1[player1_name][tournament_series])))
        print("{}, titles {} won during the year: {}".format(player2_name, tournament_series,
                                                             len(player2[player2_name][tournament_series])))
    except:
        prediction['p1'].append(0)
        prediction['p2'].append(0)
        print("{}, titles {} won during career: N/A".format(player1_name, tournament_series))
        print("{}, titles {} won during career: N/A".format(player2_name, tournament_series))

    # compare titles by series and surface during the year

    player1 = players_titles.Titles_year_serie_surface_player(player1_name, year, surface)
    player2 = players_titles.Titles_year_serie_surface_player(player2_name, year, surface)

    try:
        if len(player1[player1_name][tournament_series]) > len(player2[player2_name][tournament_series]):
            prediction['p1'].append(1.0)
        elif len(player1[player1_name][tournament_series]) < len(player2[player2_name][tournament_series]):
            prediction['p2'].append(1.0)

        print("{}, titles {} won on {} during the year: {}".format(player1_name, tournament_series, surface,
                                                                   len(player1[player1_name][tournament_series])))
        print("{}, titles {} won on {} during the year: {}".format(player2_name, tournament_series, surface,
                                                                   len(player2[player2_name][tournament_series])))
    except:
        prediction['p1'].append(0)
        prediction['p2'].append(0)
        print("{}, titles {} won during career: N/A".format(player1_name, tournament_series, surface))
        print("{}, titles {} won during career: N/A".format(player2_name, tournament_series, surface))

    # compare h2h of all time
    h2h_info = h2h.h2h_all_time(player1_name, player2_name)

    if h2h_info[0] > h2h_info[1]:
        prediction['p1'].append(0.5)
    elif h2h_info[0] < h2h_info[1]:
        prediction['p2'].append(0.5)

    h2h_matches=h2h_info[2]
    for date in h2h_matches:

        print("Date: {} - Tournament: {} - Surface: {} - Round: {} - Winner: {} - Loser: {} - Score: {}{}-{}{}-{}{}-{}{}-{}{} ".format(date, h2h_matches[date]['Tournament'], h2h_matches[date]['Surface'], h2h_matches[date]['Round'], h2h_matches[date]['Winner'], h2h_matches[date]['Loser'], h2h_matches[date]['W1'],h2h_matches[date]['L1'],h2h_matches[date]['W2'],h2h_matches[date]['L2'],h2h_matches[date]['W3'],h2h_matches[date]['L3'],h2h_matches[date]['W4'],h2h_matches[date]['L4'],h2h_matches[date]['W5'],h2h_matches[date]['L5']))

    print("H2H of all time: {} - {}".format(h2h_info[0], h2h_info[1]))

    # compare h2h on the surface of all time
    h2h_info = h2h.h2h_surface(player1_name, player2_name, surface)

    if h2h_info[0] > h2h_info[1]:
        prediction['p1'].append(1.0)
    elif h2h_info[0] < h2h_info[1]:
        prediction['p2'].append(1.0)
    print("H2H of all time on {}: {}".format(surface, h2h_info))

    # compare h2h of the year

    h2h_info = h2h.h2h_year(player1_name, player2_name, year)

    if h2h_info[0] > h2h_info[1]:
        prediction['p1'].append(1.0)
    elif h2h_info[0] < h2h_info[1]:
        prediction['p2'].append(1.0)

    print("H2H in {}: {}".format(year, h2h_info))

    # compare h2h on the surface in the year
    h2h_info = h2h.h2h_surface_year(player1_name, player2_name, surface, year)

    if h2h_info[0] > h2h_info[1]:
        prediction['p1'].append(.5)
    elif h2h_info[0] < h2h_info[1]:
        prediction['p2'].append(.5)

    print("H2H in {} in {}: {}".format(year, surface, h2h_info))


    # compare record of all time in the tournament
    player1 = players_activity.Record_career_tournament_player(player1_name, tournament_name, location)

    player2 = players_activity.Record_career_tournament_player(player2_name, tournament_name, location)

    if player1[player1_name]['Win'] > player2[player2_name]['Win']:
        prediction['p1'].append(.25)
    elif player1[player1_name]['Win'] < player2[player2_name]['Win']:
        prediction['p2'].append(.25)

    print('Record of all time in {}'.format(tournament_name))
    print(player1)
    print(player2)

    #compare average of all time in the tournament
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

    print('Average in the tournament')
    print("{}: {}%".format(player1_name,average_p1))
    print("{}: {}%".format(player2_name,average_p2))

    # compare titles in that tournament

    player1 = players_activity.Best_performance_tournament_player(player1_name, tournament_name, location)

    player2 = players_activity.Best_performance_tournament_player(player2_name, tournament_name, location)

    if player1[player1_name]['Total Titles'] > player2[player2_name]['Total Titles']:
        prediction['p1'].append(.5)
    elif player1[player1_name]['Total Titles'] < player2[player2_name]['Total Titles']:
        prediction['p2'].append(.5)
    print('Titles of all time in {}'.format(tournament_name))
    print("{}: {}".format(player1_name, player1[player1_name]['Total Titles']))
    print("{}: {}".format(player2_name, player2[player2_name]['Total Titles']))

    # Best performance in the tournament

    if player1[player1_name]['Total Titles'] == 0 and player2[player2_name]['Total Titles'] == 0:

        if player1[player1_name]['Best Performance']['Win'] > player2[player2_name]['Best Performance']['Win']:
            prediction['p1'].append(.5)
        elif player1[player1_name]['Best Performance']['Win'] < player2[player2_name]['Best Performance']['Win']:
            prediction['p2'].append(.5)

    print('Best performance and titles of all time in {}'.format(tournament_name))
    print("{}: {}".format(player1_name, player1[player1_name]['Best Performance']))
    print("{}: {}".format(player2_name, player2[player2_name]['Best Performance']))

    # performance last year in the tournament

    player1 = players_activity.Last_year_performance_tournament_player(player1_name, tournament_name, year, location)

    player2 = players_activity.Last_year_performance_tournament_player(player2_name, tournament_name, year, location)

    if player1[player1_name]['Performance']['Win'] > player2[player2_name]['Performance']['Win']:
        prediction['p1'].append(.25)
    elif player1[player1_name]['Performance']['Win'] < player2[player2_name]['Performance']['Win']:
        prediction['p2'].append(.25)

    print('Performance last year in {}'.format(tournament_name))
    print("{}: {}".format(player1_name, player1[player1_name]['Performance']))
    print("{}: {}".format(player2_name, player2[player2_name]['Performance']))


    # compare performance of all time by rounds

    player1= rounds.Record_rounds_career(player1_name, best_of)
    player2 = rounds.Record_rounds_career(player2_name, best_of)
    average_p1=0.0
    average_p2=0.0

    #compare victories of all time by round
    try:

        if player1[player1_name]['Rounds'][round]['Win'] > player2[player2_name]['Rounds'][round]['Win']:
            prediction['p1'].append(.25)

        elif player1[player1_name]['Rounds'][round]['Win'] < player2[player2_name]['Rounds'][round]['Win']:
            prediction['p2'].append(.25)
    except:
        prediction['p1'].append(0)
        prediction['p2'].append(0)

    #average of victories of all time by round
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
    print('Average of all time in {}'.format(round))
    print("Wins average of all time of {}: {}%".format(player1_name, average_p1))
    print("Wins average of all time of {}: {}%".format(player2_name, average_p2))


    print('Record of all time by rounds: ')
    print(player1_name, player1[player1_name]['Rounds'][round])
    print(player2_name, player2[player2_name]['Rounds'][round])

#-------------------------------------------------------------------------------------
    # compare performance of all time by rounds and surface
    player1 = rounds.Record_rounds_surface_career(player1_name, surface,best_of)
    player2 = rounds.Record_rounds_surface_career(player2_name, surface,best_of)

    # compare victories of all time by round and by surface

    if player1[player1_name]['Rounds'][round]['Win'] > player2[player2_name]['Rounds'][round]['Win']:
        prediction['p1'].append(.25)

    elif player1[player1_name]['Rounds'][round]['Win'] < player2[player2_name]['Rounds'][round]['Win']:
        prediction['p2'].append(.25)



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
    print('Average in {} on {}'.format(round, surface))
    print("Wins average of all time of {}: {}%".format(player1_name, average_p1))
    print("Wins average of all time of {}: {}%".format(player2_name, average_p2))



    print('Record of all time by rounds on {}: '.format(surface))
    print(player1_name, player1[player1_name]['Rounds'][round])
    print(player2_name, player2[player2_name]['Rounds'][round])

    # compare performance during the year by rounds

    player1= rounds.Record_rounds_year(player1_name, year,best_of)
    player2 = rounds.Record_rounds_year(player2_name, year,best_of)

    #compare victories of the year by round

    if player1[player1_name]['Rounds'][round]['Win'] > player2[player2_name]['Rounds'][round]['Win']:
        prediction['p1'].append(.25)

    elif player1[player1_name]['Rounds'][round]['Win'] < player2[player2_name]['Rounds'][round]['Win']:
        prediction['p2'].append(.25)

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
    print('Average in {} in {}'.format(round, year))
    print("Wins average in {} of {}: {}%".format(year, player1_name, average_p1))
    print("Wins average in {} of {}: {}%".format(year, player2_name, average_p2))


    print('Record {} by rounds: '.format(year))
    print(player1_name, player1[player1_name]['Rounds'][round])
    print(player2_name, player2[player2_name]['Rounds'][round])

    # compare performance during the year by rounds and surface

    player1 = rounds.Record_rounds_surface_year(player1_name, year, surface,best_of)
    player2 = rounds.Record_rounds_surface_year(player2_name, year, surface,best_of)

    # compare victories of the year by round by surface

    if player1[player1_name]['Rounds'][round]['Win'] > player2[player2_name]['Rounds'][round]['Win']:
        prediction['p1'].append(.25)

    elif player1[player1_name]['Rounds'][round]['Win'] < player2[player2_name]['Rounds'][round]['Win']:
        prediction['p2'].append(.25)

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
    print('Average in {} in {} on {}'.format(year, round, surface))
    print("Wins average in {} of {}: {}%".format(year, player1_name, average_p1))
    print("Wins average in {} of {}: {}%".format(year, player2_name, average_p2))

    print('Record {} by rounds on {}: '.format(year,surface))
    print(player1_name, player1[player1_name]['Rounds'][round])
    print(player2_name, player2[player2_name]['Rounds'][round])

#Show_Information(data)