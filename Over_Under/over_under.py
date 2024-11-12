import json


data_Tournament = {
    'Name_tournament' : 'Citi Open',
     # '1st Round', '2nd Round', '3rd Round', '4th Round', 'Quarterfinals', 'Semifinals', 'The Final'
    'Round':'1st Round',
    'Game_parameter': 20
}

over = 0
under = 0
games = []

#for year in range(2000, 2024, 1):
#year = str(year)
year = '2023'
name_tournament = ''
file = open('../JSON_files/ResultATP_'+year+'.json')
data = json.load(file)


for info in data:
    if data_Tournament['Name_tournament'] == info['Tournament']:
        if data_Tournament['Round'] == info['Round']:
            games = [info['W1'], info['L1'], info['W2'], info['L2'], info['W3'], info['L3'], info['W4'], info['L4'], info['W5'], info['L5']]
            # delete the empty values
            # -----------------------------------------------------------------------------
            for i in reversed(range(len(games))):
                if games[i] == '':
                    games.pop(i)
                else:
                    games[i] = int(games[i])
            # -------------------------------------------------------------------------------

            games = sum(games)
            if games > data_Tournament['Game_parameter']:
                over += 1
            if games <= data_Tournament['Game_parameter']:
                under += 1

print(data_Tournament['Round'])
print('Over = {}'.format(over))
print('Under = {}'.format(under))