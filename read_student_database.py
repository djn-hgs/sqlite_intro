import sqlite3 as sql

# This creates an sqlite file if it doesn't exist and opens it otherwise

with sql.connect('Student db/student.db') as conn:

    # The cursor is used to read and write to the database

    cursor = conn.cursor()

    # This will add a single entry to the student table

    student_read = '''
        SELECT * FROM student
        WHERE  age > ?;
        '''

    # We then execute it using cursor

    cursor.execute(student_read, ('15',))
    first = cursor.fetchone()
    second = cursor.fetchmany(2)
    third = cursor.fetchall()

    print(first)
    print(second)
    print(third)

