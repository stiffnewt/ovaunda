import nfldb
db = nfldb.connect()

q = nfldb.Query(db)
q.game(season_year=2014)
q.game(season_type='Regular')
q.game(team='MIA')

data = []

for g in q.as_games():
    results = str(g)
    data.append(results)

for i in data:
    lst = i.split()
    index = lst.index('MIA')
    nindex = index + 1
    print lst[nindex]
