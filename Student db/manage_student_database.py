import sqlite3 as sql


def get_students(cursor):
    student_read = '''
            SELECT StudentID, FirstName, LastName FROM student;
            '''

    cursor.execute(student_read)

    return cursor.fetchall()


def get_student_info(cursor, student_id):
    student_info_read = '''
            SELECT FirstName, LastName, DoB, gender
            FROM student
            WHERE StudentID = ?;
            '''

    cursor.execute(student_info_read, (student_id,))

    return cursor.fetchall()


def update_student_info(cursor, column_name, field_value, student_id):
    student_info_update = f'''
                 UPDATE student
                 SET {column_name} = ?
                 WHERE StudentID = ?;
                '''

    cursor.execute(student_info_update, (field_value, student_id))


def select_student(cursor):
    all_students = get_students(cursor)

    print()

    for s in all_students:
        print(s)

    print()

    selection_id = input('Give ID of pupil: ')

    return selection_id


def get_subjects(cursor):
    subject_read = '''
            SELECT SubjectID, Name FROM subject;
            '''

    cursor.execute(subject_read)

    return cursor.fetchall()


def get_pupil_subjects(cursor, pupil_id):
    get_pupil_subject = '''
                SELECT subject.Name
                FROM subject
                JOIN StudentSubject
                ON subject.SubjectID = StudentSubject.SubjectID
                WHERE StudentSubject.StudentID = ?
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
                SELECT house.Name, TutorGroup.Year, student.FirstName
                FROM House
                JOIN TutorGroup
                ON House.HouseID = TutorGroup.HouseID
                JOIN student
                ON student.TutorGroupID = TutorGroup.TutorGroupID
                WHERE student.StudentID =  ?;
                '''

    cursor.execute(house_read, (pupil_id,))

    return cursor.fetchall()


# This creates an sqlite file if it doesn't exist and opens it otherwise

with sql.connect('student.db') as student_db_conn:
    # The cursor is used to read and write to the database

    student_db_cursor = student_db_conn.cursor()

    while True:
        choice = input('\n'
                       'Options:\n'
                       '0 - exit\n'
                       '1 - get house\n'
                       '2 - add pupil subject\n'
                       '3 - get pupil subjects\n'
                       '4 - amend student record\n'
                       '\n'
                       'Which would you like? ')

        if choice == '0':
            break

        elif choice == '1':

            selection_pupil_id = select_student(student_db_cursor)

            print(get_house(student_db_cursor, selection_pupil_id))

        elif choice == '2':

            selection_pupil_id = select_student(student_db_cursor)

            all_subjects = get_subjects(student_db_cursor)

            for s in all_subjects:
                print(s)

            selection_subject_id = input('Add which subject? ')
            add_pupil_subject(student_db_cursor, selection_pupil_id, selection_subject_id)

        elif choice == '3':

            selection_pupil_id = select_student(student_db_cursor)

            pupil_subjects = get_pupil_subjects(student_db_cursor, selection_pupil_id)

            print()

            for s in pupil_subjects:
                print(s)

        elif choice == '4':

            selection_pupil_id = select_student(student_db_cursor)

            student_info = get_student_info(student_db_cursor, selection_pupil_id)

            print(student_info)

            choice = input('\n'
                           'Options:\n'
                           '0 - back\n'
                           '1 - change first name\n'
                           '2 - change last name\n'
                           '3 - change DoB\n'
                           '4 - set gender\n'
                           '\n'
                           'Which would you like? ')

            if choice == '1':
                new_firstname = input('\n'
                                      'FirstName? ')

                update_student_info(student_db_cursor, 'FirstName', new_firstname, selection_pupil_id)

            elif choice == '2':
                new_lastname = input('\n'
                                     'LastName? ')

                update_student_info(student_db_cursor, 'LastName', new_lastname, selection_pupil_id)

            elif choice == '3':
                new_dob = input('\n'
                                'DoB? ')

                update_student_info(student_db_cursor, 'DoB', new_dob, selection_pupil_id)

            elif choice == '4':
                new_gender = input('\n'
                                   'Gender? ')

                update_student_info(student_db_cursor, 'Gender', new_gender, selection_pupil_id)
