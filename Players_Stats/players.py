import json

year='2024'
file = open('../JSON_files/ResultATP_'+year+'.json')
data = json.load(file)
players=[]


for info in data:

    if info['Winner'] not in players:
        players.append(info['Winner'])
    if  info['Loser'] not in players:
        players.append(info['Loser'])
players.sort()
for player in players:
    print(player)