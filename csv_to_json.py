import csv
import json

year='2024'
def csv_to_json_tournaments(year):

    resultATP = []
    with open('CSV_files/TournamentATP - '+year+'.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            resultATP.append(row)
        csvfile.close()


    with open('JSON_files/ResultATP_'+year+'.json', 'w') as jsonfile:
        json.dump(resultATP,jsonfile)
        jsonfile.close()

    for info in resultATP:
        if info['ATP'] == '1':
            print(info)
            pass
        print(info)


#write all players in a json file
def csv_to_json_players(year):

    players = []
    with open('CSV_files/ATP - players.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            players.append(row)
        csvfile.close()


    with open('JSON_files/ATP - players.json', 'w') as jsonfile:
        json.dump(players,jsonfile)
        jsonfile.close()

    for info in players:

        print(info)


#remove spaces in the begining and the end of every key and value in the dictionary.
#only work with csv files
def remove_space(year):
    players = []
    with open('CSV_files/TournamentATP - '+year+'.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            players.append(row)
        csvfile.close()

#remove spaces from keys and values
    for i in range(len(players)):
        players[i] = {key.strip(): value for key, value in players[i].items()}
        players[i] = {key: value.strip() for key, value in players[i].items()}

#write a new csv file
    fields = list(players[0].keys())
    with open('CSV_files/TournamentATP - '+year+'.csv','w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fields)
        writer.writeheader()
        writer.writerows(players)
        csvfile.close()

#for year in range(2000,2024,1):
    #year=str(year)
remove_space(year)
#csv_to_json_tournaments(year)