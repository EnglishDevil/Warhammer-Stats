import pandas
import sqlite3
n = 0

cursor = sqlite3.connect('WarhammerDB.db') # I've created a "database" called WarhammerDB. you can throw data in here and connect to it with other programmes

# Let's add some data

# pandas makes this easy.  Simply "read_csv" on the CSV file. they also have read_excel, but you'd need to look into how that works
WHstatsData1_DF = pandas.read_csv(r'C:\Users\Adam\PycharmProjects\Warhammer_calculator\Tournamentreportmaster.csv', header=0)  # the data is now in Python, in this variable

#print(WHstatsData1_DF.iloc[0:2]) # look, all that sweet data.

#exit()

# It's in python memory now, but we need to store it incase you make another program that wants to use, or in case another user or system wants to access it.

# using the ".to_sql" method on the dataframe moves the data into an SQL table. This is absolute magic and saves loads of work
WHstatsData1_DF.to_sql('WHstatsData_table', # table name
                        con=cursor, #this is the connection - where to put the table i.e. in your database
                        if_exists='replace') # this tells it to replace the table if it already exists. you could instead make it append the data to the end of the table

# lets check what is in this table
WHstatsData_fromTable = cursor.execute('''SELECT DISTINCT faction FROM WHstatsData_table''')

Distinctfaction = WHstatsData_fromTable.fetchall()

# We've got the data from the table in a variable, now lets go over all the rows and print what we have:
for faction in Distinctfaction:
    print(str(n) + " " + str(faction[0]))
    n += 1

for letter in ["envelope"]:
    print(letter)

#
# cursor.execute('''CREATE TABLE WHStats_Data1_table (
#                     [Player] [nvarchar](50) NULL,
#                     [Faction] [nvarchar](50) NULL,
#                     [Faction Detachment] [nvarchar](50) NULL,
#                     [Primary] [int] NULL,
#                     [Secondary] [int] NULL,
#                     [Unique Faction List] [int] NULL,
#                     [Chapter] [int] NULL,
#                     [ChapterDetachment] [int] NULL,
#                     [Unique Chapter List] [int] NULL,
#                     [Wins] [int] NULL,
#                     [Losses] [int] NULL,
#                     [Draws] [int] NULL,
#                     [Games] [int] NULL,
#                     [Avg VP] [decimal](5,2) NULL,
#                     [Avg Oppon VP] [decimal](5,2) NULL,
#                     [Win Percentage] [decimal](5,2) NULL,
#                     [Games by Primary] [int] NULL,
#                     [Games by Secondary] [int] NULL,
#                     [Win % By Faction] [decimal](5,2) NULL,
#                     [VP by Faction] [decimal](5,2) NULL,
#                     [Opp VP by Faction] [decimal](5,2) NULL,
#                     [Win % By Primary] [decimal](5,2) NULL,
#                     [Win % by Chapter] [decimal](5,2) NULL,
#                     [VP by Primary] [decimal](5,2) NULL,
#                     [Top List] [nvarchar](50) NULL,
#                     [Tournament] [nvarchar](50) NULL,
#                     [Ruleset] [nvarchar](50) NULL,
#                     [Date] [Date] NULL)''')
#
# cursor.execute('''INSERT INTO WHStats_Data1_table VALUES (''')



