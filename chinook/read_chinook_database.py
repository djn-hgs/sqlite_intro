import sqlite3 as sql

# This creates an sqlite file if it doesn't exist and opens it otherwise

with sql.connect('chinook.db') as conn:

    # The cursor is used to read and write to the database

    cursor = conn.cursor()

    # This will add a single entry to the student table

    chinook_read = '''
        SELECT Title, Name FROM albums JOIN artists
        ON albums.ArtistId = artists.ArtistId;
        '''

    # We then execute it using cursor

    cursor.execute(chinook_read)
    first = cursor.fetchone()
    second = cursor.fetchmany(2)
    third = cursor.fetchall()

    print(first)
    print(second)
    for item in third:
        print(item)

