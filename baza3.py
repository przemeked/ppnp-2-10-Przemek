import sqlite3

try:
    sql_connection = sqlite3.connect('sqlite_python2.db')
    # insert_sql = "INSERT INTO software (id, name, price) VALUES (1, 'Python', '100000');"
    select = '''
    SELECT * FROM software;
    '''
    cursor = sql_connection.cursor()
    print("Baza danych została podłączona")
    # cursor.execute(insert_sql)
    # sql_connection.commit()

    for row in cursor.execute(select):
        print(row)

except sqlite3.Error as e:
    print("błąd podczas podłączania bazy danych", e)
finally:
    if sql_connection:
        sql_connection.close()
        print("Baza danyc zostala zamknieta")
