import sqlite3

sqliteConnection = sqlite3.connect('InventorySystem-TEST.db')

cursor = sqliteConnection.cursor()

sql_command = """
CREATE TABLE TEST(
    name INTEGER PRIMARY KEY,
    email VARCHAR(20)
);
"""

cursor.execute(sql_command)

print("sql commnd executed")