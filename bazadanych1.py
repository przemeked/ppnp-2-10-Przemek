import sqlite3

try:
    sql_connection = sqlite3.connect('sqlite_python.db')
    cursor = sql_connection.cursor()
    print("Baza danych została podłączona")
except sqlite3.Error as e:
    print("błąd podczas podłączania bazy danych")
finally:
    if sql_connection:
        sql_connection.close()
        print("Baza danyc zostala zamknieta")
