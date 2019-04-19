import numpy as np
import pandas as pd
statstable = pd.read_csv('Tournament.csv', delimiter = ',')
statstable[statstable.Player == 'David Rodriguez'][['Faction', 'Player', 'VP by Faction', 'Win % By Faction', 'Wins', 'Losses']]
facgroup = statstable.groupby('Faction').sum()[['Faction Detachment', 'Wins', 'Losses', 'Draws', 'Games']]
facgroup.sort_values('Games',ascending=False)
statstable.sort_values('Win % By Faction',ascending=False)
x = ((facgroup['Wins']) / (facgroup['Games']))*100
print (x)
facgroup['Win Percentage'] = x
winper_table = facgroup.round(1)
winper_table.sort_values('Win Percentage',ascending=False)
