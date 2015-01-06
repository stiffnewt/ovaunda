import nfldb

#connect to nfldb database
db = nfldb.connect()

#select home & away teams
#TODO: add error checking for wrong input
hteam = raw_input('enter home team (e.g. "MIA" or "NE"): ')
ateam = raw_input('enter away team (e.g. "MIA" or "NE"): ')

#query the database for home team
#TODO: make a function for the home & away queries or can I combine
#the queries to not duplicate??
q = nfldb.Query(db)
q.game(season_year = 2014)
q.game(season_type = 'Regular').sort(('week', 'asc'))
q.game(team = hteam)

#convert results of hteam query to strings in a list
hweekly = []
for week in q.as_games():
    results = str(week)
    hweekly.append(results)

#query the database for away team
q = nfldb.Query(db)
q.game(season_year = 2014)
q.game(season_type = 'Regular').sort(('week', 'asc'))
q.game(team = ateam)

#convert results of ateam query to strings in a list
aweekly = []
for week in q.as_games():
    results = str(week)
    aweekly.append(results)

#Testing, TODO remove
print hweekly
print aweekly

#counters
score_h = 0
score_a = 0

#loop through weekly games & obtain total score to date for season
#TODO: create a function for these

for game in hweekly:
    #turn weekly game string into a list
    mk_str_lst = game.split()
    #find the team's name in the list
    find_team = mk_str_lst.index(hteam)
    #find team's score which is next in list
    score_h = score_h + float(mk_str_lst[find_team + 1].strip('()'))

for game in aweekly:
    #turn weekly game string into a list
    mk_str_lst = game.split()
    #find the team's name in the list
    find_team = mk_str_lst.index(ateam)
    #find team's score which is next in list
    score_a = score_a + float(mk_str_lst[find_team + 1].strip('()'))

avg_score_h = score_h / len(hweekly)
avg_score_a = score_a / len(aweekly)

#testing, TODO remove
print avg_score_h
print avg_score_a

#average 'points for' for the home and away team
print (avg_score_h + avg_score_a) / 2
