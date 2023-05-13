from database.db_conn import session
from database.db_models import Group, Student, Teacher, Class, Mark
from create_fake_data import generate_fake_data, prepare_data


NUMBER_CLASSES = 6
NUMBER_STUDENTS = 50
NUMBER_GROUPS = 3
NUMBER_TEACHERS = 5

if __name__ == '__main__':
    groups, students, teachers, classes, marks = prepare_data(*generate_fake_data(NUMBER_STUDENTS, NUMBER_TEACHERS))
    print(groups, students, teachers, classes, marks)
    for group in groups:
        print(group)
        g = Group(group_name=group[0])
        session.add(g)
        session.commit()

    for student in students:
        print(student)
        name = student[0].split()
        f_name = name[-2]
        l_name = name[-1]
        group_id = student[1]
        s = Student(first_name=f_name, last_name=l_name, group_id=group_id)
        session.add(s)
        session.commit()


    for teacher in teachers:
        print(teacher)
        name = teacher[0].split()
        f_name = name[-2]
        l_name = name[-1]

        t = Teacher(first_name=f_name, last_name=l_name)
        session.add(t)
        session.commit()

    for cl in classes:
        print(cl)
        class_name = cl[0]
        teacher_id = cl[1]

        c = Class(class_name=class_name, teacher_id=teacher_id)
        session.add(c)
        session.commit()

    for mark in marks:
        print(mark)
        mrk = mark[0]
        date = mark[1]
        class_id = mark[2]
        student_id = mark[3]

        m = Mark(mark=mrk, date=date, class_id=class_id, student_id=student_id)
        session.add(m)
        session.commit()