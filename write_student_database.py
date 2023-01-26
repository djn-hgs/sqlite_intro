import sqlite3 as sql

# This creates an sqlite file if it doesn't exist and opens it otherwise

with sql.connect('Student db/student.db') as conn:

    # The cursor is used to read and write to the database

    cursor = conn.cursor()

    # This will add a single entry to the student table

    single_student_add = '''
        INSERT INTO student (firstname, lastname, age, gender)
        VALUES ('Wednesday', 'Addams', 16, 'Female');
        '''

    # We then execute it using cursor

    cursor.execute(single_student_add)

    # We can also do this in a tidier way using placeholders

    multi_student_add = '''
            INSERT INTO student (firstname, lastname, age, gender)
            VALUES (?, ?, ?, ?);
            '''

    cursor.execute(multi_student_add, ('Enid', 'Sinclair', 16, 'Female'))

    # If you want to add loads then just use a list!

    more_names = [
        ('Xavier', 'Thorpe', 17, 'Male'),
        ('Tyler', 'Galpin', 18, 'Male')
    ]

    # It is pretty clear what execeutemany does

    cursor.executemany(multi_student_add, more_names)
