import sqlite3

con = sqlite3.connect('db.sqlite3')
cursorObj = con.cursor()

def sql_fetch(con):
 
    cursorObj = con.cursor()
 
    cursorObj.execute('SELECT name from sqlite_master where type= "table"')
 
    print(cursorObj.fetchall())
 
sql_fetch(con)

cursorObj.execute('select * from projects_projectimage')
print(cursorObj.fetchall())

#project = '"Vijgen met kaas"' 
#omschrijving = '"Camembert and ricotta cheese in the oven together with fresh figs, honey, oregano, bay leaves, olive oil and salt/peper. After 30/40 minutes the camembert is melted and figs are soft: perfect match on a slice of bread/toast. Try it as a starter together with some good wines or beers"'
#ingredienten = '[Verse vijgen, Camembert, Ricotta, Honing, Oregano, Laurier]'
#afbeelding = '"img/vijgen.png"'
#
#toevoegen = 'Insert into projects_project(title, description, technology, image) Values (' + project +', ' + omschrijving + ', '+ ingredienten+ ', ' + afbeelding +')'
#
#
#
#cursorObj.execute('%s'%toevoegen)
#con.commit()
