import sqlite3 as sql

# This creates an sqlite file if it doesn't exist and opens it otherwise
# The extension is a matter of personal preference
# Using the with statement avoids the need to close the connection
# This can be achieved with conn.close() otherwise

with sql.connect('student.db') as conn:

    # The cursor is used to read and write to the database

    cursor = conn.cursor()

    # Here is an SQL query in the sqlite3 dialect
    # Note the IF NOT EXISTS to avoid errors

    create_student_table = '''
        CREATE TABLE IF NOT EXISTS student (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            firstname TEXT NOT NULL,
            lastname TEXT NOT NULL,
            age INTEGER,
            gender TEXT
        );
        '''

    # We then execute it using cursor

    cursor.execute(create_student_table)

