import sqlite3

try:
    sql_connection = sqlite3.connect('sqlite_python2.db')
    query = '''
    CREATE TABLE developers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL, 
    email TEXT NOT NULL UNIQUE,
    joining_date DATETIME,
    salary REAL NOT NULL);
    '''
    with open('tables.sql', 'r') as file:
            sql_script = file.read()

    cursor = sql_connection.cursor()
    print("Baza danych została podłączona1")
    cursor.executescript(sql_script)

    # cursor.execute(query)
    # sql_connection.commit()
except sqlite3.Error as e:
    print("błąd podczas podłączania bazy danych1", e)
finally:
    if sql_connection:
        sql_connection.close()
        print("Baza danyc zostala zamknieta")

