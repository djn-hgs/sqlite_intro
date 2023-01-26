import sqlite3 as sql

# This creates an sqlite file if it doesn't exist and opens it otherwise

with sql.connect('student.db') as conn:

    # The cursor is used to read and write to the database

    cursor = conn.cursor()

    # This will add a single entry to the student table

    student_read = '''
        SELECT * FROM student;
        '''

    # We then execute it using cursor

    cursor.execute(student_read)
    all_students = cursor.fetchall()

    print(all_students)
