
#import sys
#sys.path.insert(0,"C:\\Users\\alexa\\Documents\\Python Scripts\\Sybil\\Tennis\\Predictions\\")

import show_info
from Tennis.Predictions import prediction, prediction2, prediction3, prediction4, prediction5, prediction6, \
    prediction7, prediction8, prediction9, prediction10, prediction11, prediction12, prediction13, prediction14, prediction15
from Tennis.Sets_Prediction import prediction_sets
from Tennis.Games_Prediction import prediction_games


data = {
    'player1_name':'Michelsen A.',
    'player2_name':'Kovacevic A.',
    'surface':'Grass',
    # Serie's tornaments: ATP250 - ATP500 - Masters 1000 - Grand Slam
    'tournament_series':'ATP250',
    'tournament_name':'',
    'location':'',
    'year':'2024',
    'best of':'3',
    # '1st Round', '2nd Round', '3rd Round', '4th Round', 'Quarterfinals', 'Semifinals', 'The Final'
    'round': '4th Round',
    'games_parameter':37
}

'''
data = {
    'player1_name':'Sinner J.',
    'player2_name':'Medvedev D.',
    'surface':'Hard',
    # Serie's tornaments: ATP250 - ATP500 - Masters 1000 - Grand Slam
    'tournament_series':'ATP250',
    'tournament_name':'Brisbane International',
    'location':'Brisbane',
    'year':'2023',
    'best of':'3',
    # '1st Round', '2nd Round', '3rd Round', '4th Round', 'Quarterfinals', 'Semifinals', 'The Final'
    'round': '1st Round',
    'games_parameter':37
}

'''
prediction_p1=0
prediction_p2=0

show_info.Show_Information(data)
print("\n--------------------------------------------------------------------------------------------------\n")

result = prediction.Match_Predictor(data)
if sum(result['p1']) > sum(result['p2']):
    prediction_p1 += 1
elif sum(result['p1']) < sum(result['p2']):
    prediction_p2 += 1

result = prediction2.Match_Predictor(data)
if sum(result['p1']) > sum(result['p2']):
    prediction_p1 += 1
elif sum(result['p1']) < sum(result['p2']):
    prediction_p2 += 1
'''
result = prediction3.Match_Predictor(data)
if sum(result['p1']) > sum(result['p2']):
    prediction_p1 += 1
elif sum(result['p1']) < sum(result['p2']):
    prediction_p2 += 1

result = prediction4.Match_Predictor(data)
if sum(result['p1']) > sum(result['p2']):
    prediction_p1 += 1
elif sum(result['p1']) < sum(result['p2']):
    prediction_p2 += 1

result = prediction5.Match_Predictor(data)
if sum(result['p1']) > sum(result['p2']):
    prediction_p1 += 1
elif sum(result['p1']) < sum(result['p2']):
    prediction_p2 += 1

result = prediction6.Match_Predictor(data)
if sum(result['p1']) > sum(result['p2']):
    prediction_p1 += 1
elif sum(result['p1']) < sum(result['p2']):
    prediction_p2 += 1

result = prediction7.Match_Predictor(data)
if sum(result['p1']) > sum(result['p2']):
    prediction_p1 += 1
elif sum(result['p1']) < sum(result['p2']):
    prediction_p2 += 1

result = prediction8.Match_Predictor(data)
if sum(result['p1']) > sum(result['p2']):
    prediction_p1 += 1
elif sum(result['p1']) < sum(result['p2']):
    prediction_p2 += 1

result = prediction9.Match_Predictor(data)
if sum(result['p1']) > sum(result['p2']):
    prediction_p1 += 1
elif sum(result['p1']) < sum(result['p2']):
    prediction_p2 += 1

result = prediction10.Match_Predictor(data)
if sum(result['p1']) > sum(result['p2']):
    prediction_p1 += 1
elif sum(result['p1']) < sum(result['p2']):
    prediction_p2 += 1


result = prediction11.Match_Predictor(data)
if sum(result['p1']) > sum(result['p2']):
    prediction_p1 += 1
elif sum(result['p1']) < sum(result['p2']):
    prediction_p2 += 1

result = prediction12.Match_Predictor(data)
if sum(result['p1']) > sum(result['p2']):
    prediction_p1 += 1
elif sum(result['p1']) < sum(result['p2']):
    prediction_p2 += 1

result = prediction13.Match_Predictor(data)
if sum(result['p1']) > sum(result['p2']):
    prediction_p1 += 1
elif sum(result['p1']) < sum(result['p2']):
    prediction_p2 += 1
 

result = prediction14.Match_Predictor(data)
if sum(result['p1']) > sum(result['p2']):
    prediction_p1 += 1
elif sum(result['p1']) < sum(result['p2']):
    prediction_p2 += 1
   '''
result = prediction15.Match_Predictor(data)
if sum(result['p1']) > sum(result['p2']):
    prediction_p1 += 1
elif sum(result['p1']) < sum(result['p2']):
    prediction_p2 += 1

print('The total for {} is: {} '.format(data['player1_name'], prediction_p1))
print('The total for {} is: {} '.format(data['player2_name'], prediction_p2))

print("\n------------------------------------SETS--------------------------------------------------------------\n")

prediction_sets.Sets_Predictor(data)

print("\n------------------------------------GAMES--------------------------------------------------------------\n")

prediction_games.Games_Predictor(data)




