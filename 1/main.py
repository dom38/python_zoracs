import database

connection = database.database()
connection.send('payload')
connection.send('payload')
connection.retrieve()