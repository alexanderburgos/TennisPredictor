import json
tournaments = {}
Location=''

for year in range(2000, 2024, 1):

    year = str(year)

    file = open('../JSON_files/ResultATP_'+year+'.json')
    data = json.load(file)



    for info in data:


        if 'Cabos' in info['Location'] :
            print(info)
            pass

        if info['Series']=='ATP250':
            #print(info)
            pass

        if info['Tournament'] not in tournaments:
            tournaments[info['Tournament']] = {'Location':'', 'Series':'','Surface':'','Date':''}

    for info in data:

        if info['Tournament'] in tournaments:
            tournaments[info['Tournament']]['Location'] = info['Location']
            tournaments[info['Tournament']]['Series'] = info['Series']
            tournaments[info['Tournament']]['Surface'] = info['Surface']
            tournaments[info['Tournament']]['Date'] = info['Date']


sorted_titles = sorted(tournaments.items(), key = lambda x:x[1]['Surface'], reverse=True)
tournaments=dict(sorted_titles)



for tournament in tournaments:
    if tournaments[tournament]['Location']== 'Hon':
        #print(tournament,tournaments[tournament])
        pass




#print(tournaments)