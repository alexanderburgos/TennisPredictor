import json

h2h = {}
player1_name = 'Djokovic N.'
player2_name = 'Alcaraz C.'
surface = 'Grass'
year='2023'

#It doesn't include matches out of the circuit like Olympic games, copa davis, etc.
#Get h2h of all time.
def h2h_all_time(player1_name, player2_name):
    p1_victories = 0
    p2_victories = 0
    for year in range(2000,2024,1):
        year=str(year)
        file = open('../JSON_files/ResultATP_'+year+'.json')
        data = json.load(file)

        for info in data:
            if info['Winner'] == player1_name and info['Loser'] == player2_name:
                h2h[info['Date']]=info
                p1_victories +=1

            if info['Winner'] == player2_name and info['Loser'] == player1_name:
                h2h[info['Date']]=info
                p2_victories +=1
    for date in h2h:
        pass
        #print("Date: {} - Tournament: {} - Winner: {} - Loser: {} - Score: {}{}-{}{}-{}{}-{}{}-{}{} ".format(date, h2h[date]['Tournament'], h2h[date]['Winner'], h2h[date]['Loser'], h2h[date]['W1'],h2h[date]['L1'],h2h[date]['W2'],h2h[date]['L2'],h2h[date]['W3'],h2h[date]['L3'],h2h[date]['W4'],h2h[date]['L4'],h2h[date]['W5'],h2h[date]['L5']))

    #print("{} = {} \n{} = {} ".format(player1_name, p1_victories, player2_name, p2_victories))
    return p1_victories,p2_victories, h2h


#Get h2h of the current year
def h2h_year(player1_name, player2_name,year):
    p1_victories = 0
    p2_victories = 0
    file = open('../JSON_files/ResultATP_'+year+'.json')
    data = json.load(file)

    for info in data:
        if info['Winner'] == player1_name and info['Loser'] == player2_name:
            h2h[info['Date']]=info
            p1_victories +=1

        if info['Winner'] == player2_name and info['Loser'] == player1_name:
            h2h[info['Date']]=info
            p2_victories +=1
    for date in h2h:
        pass
        #print("Date: {} - Tournament: {} - Winner: {} - Loser: {} - Score: {}{}-{}{}-{}{}-{}{}-{}{} ".format(date, h2h[date]['Tournament'], h2h[date]['Winner'], h2h[date]['Loser'], h2h[date]['W1'],h2h[date]['L1'],h2h[date]['W2'],h2h[date]['L2'],h2h[date]['W3'],h2h[date]['L3'],h2h[date]['W4'],h2h[date]['L4'],h2h[date]['W5'],h2h[date]['L5']))

    #print("{} = {} \n{} = {} ".format(player1_name, p1_victories, player2_name, p2_victories))

    return p1_victories,p2_victories

#Get h2h by surface
def h2h_surface(player1_name, player2_name, surface):
    p1_victories = 0
    p2_victories = 0
    for year in range(2000,2024,1):
        year=str(year)
        file = open('../JSON_files/ResultATP_'+year+'.json')
        data = json.load(file)

        for info in data:
            if info['Winner'] == player1_name and info['Loser'] == player2_name and info['Surface'] == surface:
                h2h[info['Date']]=info
                p1_victories +=1

            if info['Winner'] == player2_name and info['Loser'] == player1_name and info['Surface'] == surface:
                h2h[info['Date']]=info
                p2_victories +=1
    for date in h2h:
        pass
        #print("Date: {} - Tournament: {} - Winner: {} - Loser: {} - Score: {}{}-{}{}-{}{}-{}{}-{}{} ".format(date, h2h[date]['Tournament'], h2h[date]['Winner'], h2h[date]['Loser'], h2h[date]['W1'],h2h[date]['L1'],h2h[date]['W2'],h2h[date]['L2'],h2h[date]['W3'],h2h[date]['L3'],h2h[date]['W4'],h2h[date]['L4'],h2h[date]['W5'],h2h[date]['L5']))

    #print("{} = {} \n{} = {} ".format(player1_name, p1_victories, player2_name, p2_victories))

    return p1_victories, p2_victories

def h2h_surface_year(player1_name, player2_name, surface, year):
    p1_victories = 0
    p2_victories = 0

    file = open('../JSON_files/ResultATP_'+year+'.json')
    data = json.load(file)

    for info in data:
        if info['Winner'] == player1_name and info['Loser'] == player2_name and info['Surface'] == surface:
            h2h[info['Date']]=info
            p1_victories +=1

        if info['Winner'] == player2_name and info['Loser'] == player1_name and info['Surface'] == surface:
            h2h[info['Date']]=info
            p2_victories +=1
    for date in h2h:
        pass
        #print("Date: {} - Tournament: {} - Winner: {} - Loser: {} - Score: {}{}-{}{}-{}{}-{}{}-{}{} ".format(date, h2h[date]['Tournament'], h2h[date]['Winner'], h2h[date]['Loser'], h2h[date]['W1'],h2h[date]['L1'],h2h[date]['W2'],h2h[date]['L2'],h2h[date]['W3'],h2h[date]['L3'],h2h[date]['W4'],h2h[date]['L4'],h2h[date]['W5'],h2h[date]['L5']))

    #print("{} = {} \n{} = {} ".format(player1_name, p1_victories, player2_name, p2_victories))

    return p1_victories, p2_victories

#h2h_all_time(player1_name, player2_name)
#h2h_year(player1_name, player2_name,year)
#h2h_surface(player1_name,player2_name,surface)
#h2h_surface_year(player1_name, player2_name, surface, year)