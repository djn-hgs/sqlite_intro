import sqlite3 as sql


def get_students(cursor):
    student_read = '''
            SELECT * FROM student;
            '''

    cursor.execute(student_read)

    return cursor.fetchall()

def get_house(cursor, pupil_id):
    house_read = '''
                SELECT house.Name, TutorGroup.Year, student.firstname
                FROM House join TutorGroup
                on House.ID = TutorGroup.HouseID
                join student
                on student.TutorGroupID = TutorGroup.ID
                where student.id =  ?;
                '''

    cursor.execute(house_read, (pupil_id,))

    return cursor.fetchall()


# This creates an sqlite file if it doesn't exist and opens it otherwise

with sql.connect('student.db') as conn:

    # The cursor is used to read and write to the database

    cursor = conn.cursor()

    all_students = get_students(cursor)

    for s in all_students:
        print(s)

    pupil_id = input('Give ID of pupil: ')

    print(get_house(cursor, pupil_id))

