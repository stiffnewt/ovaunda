import nfldb

#connect to nfldb database
db = nfldb.connect()

#select home & away teams
#TODO: add error checking for wrong input
hteam = raw_input('enter home team (e.g. "MIA" or "NE"): ')
ateam = raw_input('enter away team (e.g. "MIA" or "NE"): ')
OUscore = float(raw_input('O/U scare: '))

#query the database for home team
#TODO create better variable & argument names?
def query_the_db(HorA):
    q = nfldb.Query(db)
    q.game(season_year = 2014)
    q.game(season_type = 'Regular').sort(('week', 'asc'))
    q.game(team = HorA)

    #convert results of query to strings in a list
    weekly = []
    for week in q.as_games():
        results = str(week)
        weekly.append(results)
    return weekly

hweekly = query_the_db(hteam)
aweekly = query_the_db(ateam)

#loop through weekly games & obtain total score to date for season
#TODO: create better variable & argument names?
def get_avg_score(HorA_weekly, HorA_team):
    count_score = 0
    for game in (HorA_weekly):
        week = game.split()
        locateTeam = week.index(HorA_team)
        count_score = count_score + float(week[locateTeam + 1].strip('()'))
    return count_score / len(HorA_weekly)

hteam_avg_score = get_avg_score(hweekly, hteam)
ateam_avg_score = get_avg_score(aweekly, ateam)

print hteam, hteam_avg_score
print ateam, ateam_avg_score

#average 'points for' for the home and away team
ovaunda =  (hteam_avg_score + ateam_avg_score)

print "ovaunda says: ", ovaunda
print "Vegas says: ", OUscore

if ovaunda > OUscore:
    if (ovaunda - OUscore) > 3:
        print "go for the over with good confidence!"
    else:
        print "could go either way - the over is more likely."
elif (ovaunda < OUscore):
    if (OUscore - ovaunda) > 3:
        print "go for the under with good confidence!"
    else:
        print "could go either way - the under is more likely."
else:
    print "ovaunda and Vegas are on the same page - who knows..."
