import sqlite3 as sql


def get_students(cursor):
    student_read = '''
            SELECT * FROM student;
            '''

    cursor.execute(student_read)

    return cursor.fetchall()


def get_subjects(cursor):
    subject_read = '''
            SELECT * FROM subject;
            '''

    cursor.execute(subject_read)

    return cursor.fetchall()


def get_pupil_subjects(cursor, pupil_id):
    get_pupil_subject = '''
                SELECT subject.Name
                FROM subject JOIN StudentSubject
                ON subject.SubjectID = StudentSubject.SubjectID
                JOIN student
                ON StudentSubject.StudentID = student.id
                WHERE student.id = ?
                '''

    cursor.execute(get_pupil_subject, (pupil_id,))

    return cursor.fetchall()


def add_pupil_subject(cursor, pupil_id, subject_id):
    subject_add = '''
            INSERT INTO StudentSubject (StudentID, SubjectID)
            VALUES (?, ?);
            '''

    cursor.execute(subject_add, (pupil_id, subject_id))


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

with sql.connect('student.db') as student_db_conn:
    # The cursor is used to read and write to the database

    student_db_cursor = student_db_conn.cursor()

    while True:
        all_students = get_students(student_db_cursor)

        for s in all_students:
            print(s)

        selection_pupil_id = input('Give ID of pupil: ')
        choice = input('Options:\n'
                       '1 - get house\n'
                       '2 - add pupil subject\n'
                       '3 - get pupil subjects')

        if choice == '1':
            print(get_house(student_db_cursor, selection_pupil_id))

        if choice == '2':
            all_subjects = get_subjects(student_db_cursor)

            for s in all_subjects:
                print(s)

            subject_id = input('Add which subject? ')
            add_pupil_subject(student_db_cursor, selection_pupil_id, subject_id)

        if choice == '3':
            pupil_subjects = get_pupil_subjects(student_db_cursor, selection_pupil_id)

            for s in pupil_subjects:
                print(s)

