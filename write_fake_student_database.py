import sqlite3 as sql
import faker as f
import random as r

gb_faker = f.Faker('en_GB')
r.seed(4321)
gb_faker.random.seed(4321)

# This creates an sqlite file if it doesn't exist and opens it otherwise

with sql.connect('Student db/student.db') as conn:

    # The cursor is used to read and write to the database

    cursor = conn.cursor()

    # This will add a single entry to the student table

    single_student_add = '''
        INSERT INTO student (FirstName, LastName, age, gender)
        VALUES ('Wednesday', 'Addams', 16, 'Female');
        '''

    # We then execute it using cursor

    cursor.execute(single_student_add)

    # We can also do this in a tidier way using placeholders

    multi_student_add = '''
            INSERT INTO student (FirstName, LastName, age, gender)
            VALUES (?, ?, ?, ?);
            '''

    cursor.execute(multi_student_add, ('Enid', 'Sinclair', 16, 'Female'))

    # If you want to add loads then just use a list!

    for _ in range(10):
        firstname = gb_faker.first_name()
        lastname = gb_faker.last_name()
        age = r.randint(11, 18)
        gender = r.choice(('male', 'female'))
        cursor.execute(multi_student_add,
                       (firstname, lastname, age, gender))

    # It is pretty clear what execeutemany does
