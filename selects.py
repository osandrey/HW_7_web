from database.db_conn import session
from database.db_models import Group, Student, Teacher, Class, Mark
from sqlalchemy import select, func, desc

"""
Замість скрипту seed.py подумайте та реалізуйте повноцінну CLI програму для CRUD операцій із базою даних.
Використовуйте для цього модуль argparse .

Використовуйте команду --action або скорочений варіант -a для CRUD операцій.
Та команду --model (-m) для вказівки над якою моделлю проводитися операція.
"""

def sql_1():
    """ Знайти 5 студентів із найбільшим середнім балом з усіх предметів."""
    """
    SELECT s.fullname, ROUND(AVG(m.mark), 2) as result_mark
    FROM marks m
    LEFT JOIN students s ON s.id = m.student_id
    GROUP BY s.fullname
    ORDER BY result_mark DESC
    LIMIT 5;
    """
    result = session.query(Student.first_name, Student.last_name,
                           func.avg(Mark.mark)).join(Mark).group_by(Student.id).limit(5).all()
    answer_dict = {}
    for r in result:

        answer_dict[r[0]+" "+r[1]] = int(r[-1])

    print(result)
    print(answer_dict)

def sql_2(class_id=1):
    """Знайти студента із найвищим середнім балом з певного предмета."""

    result = session.query(Student.first_name, Student.last_name, Class.class_name, func.avg(Mark.mark))\
        .join(Class).join(Student).\
        filter(Class.id==class_id).group_by(Class.id, Student.id).order_by(desc(func.avg(Mark.mark))).first()


    answer = f'{result[0]} {result[1]} : {result[-2]}:{int(result[-1])}'


    print(answer)

def sql_3(class_id=2):
    """Знайти середній бал у групах з певного предмета."""

    result = session.query(Class.class_name, Group.group_name, func.avg(Mark.mark))\
        .select_from(Class).join(Mark).join(Student).join(Group)\
        .filter(Class.id==class_id).group_by(Class.id, Group.id).all()

    print(result)


def sql_4():
    """Знайти середній бал на потоці (по всій таблиці оцінок)."""
    result = session.query(func.avg(Mark.mark)) \
        .select_from(Mark).all()

    print(result)

def sql_5(couch=4):
    """Знайти які курси читає певний викладач."""
    """SELECT t.fullname, c.class_name as result
FROM classes c
JOIN teachers t ON t.id = c.teacher_id
WHERE t.id = 1"""
    result = session.query(Teacher.first_name, Teacher.last_name,Class.class_name)\
        .join(Class, Teacher.id==Class.teacher_id).filter(Teacher.id==couch).group_by(Teacher.id, Class.id).all()
    print(result)

def sql_6(group=2):
    """Знайти список студентів у певній групі."""
    """SELECT s.fullname, g.group_name as result
FROM groups g
JOIN students s ON g.id = s.group_id
WHERE g.id = 3"""
    result = session.query(Student.first_name, Student.last_name, Group.group_name)\
        .join(Group, Group.id==Student.group_id).filter(Group.id==group).group_by(Student.id, Group.id).all()
    print(result)

def sql_7(group=3, clas=3):
    """Знайти оцінки студентів у окремій групі з певного предмета."""
    """
    SELECT m.mark, s.fullname, g.group_name, c.class_name
    FROM marks m
    JOIN students s ON s.id = m.student_id
    JOIN groups g ON g.id = s.group_id
    JOIN classes c ON c.id = m.class_id
    WHERE g.id = 3 AND c.id = 3
    """

    result = session.query(Mark.mark, Student.first_name, Student.last_name, Group.group_name, Class.class_name) \
        .join(Student, Student.id == Mark.student_id).join(Group, Group.id == Student.group_id).join(Class, Class.id == Mark.class_id)\
        .filter(Group.id == group, Class.id == clas).all()
    print(result)


def sql_8(couch=1):
    """Знайти середній бал, який ставить певний викладач зі своїх предметів."""
    """SELECT t.fullname, ROUND(AVG(m.mark), 2)
    FROM marks m
    JOIN classes c ON c.id = m.class_id
    JOIN teachers t ON t.id = c.teacher_id
    WHERE t.id = 1
    GROUP BY c.class_name
    """
    result = session.query(Teacher.first_name, Teacher.last_name, func.round(func.avg(Mark.mark), 2)).select_from(Mark)\
        .join(Class, Class.id == Mark.class_id).join(Teacher, Teacher.id == Class.teacher_id)\
        .filter(Teacher.id == couch).group_by(Teacher.first_name, Teacher.last_name).all()
    print(result)

def sql_9(student=2):
    """Знайти список курсів, які відвідує певний студент."""
    """SELECT s.fullname, c.class_name
    FROM marks m
    JOIN classes c ON c.id = m.class_id
    JOIN students s ON s.id = m.student_id
    WHERE s.id = 1
    GROUP BY c.class_name"""

    result = session.query(Student.first_name, Student.last_name, Class.class_name).select_from(Mark) \
        .join(Class, Class.id == Mark.class_id).join(Student, Student.id == Mark.student_id) \
        .filter(Student.id == student).group_by(Student.first_name, Student.last_name, Class.class_name).all()
    print(result)

def sql_10(student=2, teacher=3):
    """Список курсів, які певному студенту читає певний викладач."""
    """SELECT c.class_name
    FROM marks m
    JOIN teachers t ON t.id = c.teacher_id
    JOIN students s ON s.id = m.student_id
    JOIN classes c ON c.id = m.class_id
    WHERE s.id = 1 AND t.id = 4"""

    result = session.query(Class.class_name).select_from(Mark) \
        .join(Class, Class.id == Mark.class_id).join(Student, Student.id == Mark.student_id).join(Teacher, Teacher.id == Class.teacher_id) \
        .filter(Student.id == student, Teacher.id == teacher).all()
    print(result)

def sql_11(student=2, teacher=3):
    """Средний балл, который определенный преподаватель ставит определенному студенту."""
    """
    SELECT t.fullname, s.fullname, c.class_name, ROUND(AVG(m.mark), 2) 
    FROM marks m
    JOIN teachers t ON t.id = c.teacher_id
    JOIN students s ON s.id = m.student_id
    JOIN classes c ON c.id = m.class_id
    WHERE t.id = 1 AND s.id = 4
    """
    result = session.query(func.round(func.avg(Mark.mark), 2)).select_from(Mark) \
        .join(Class, Class.id == Mark.class_id)\
        .join(Student, Student.id == Mark.student_id)\
        .join(Teacher, Teacher.id == Class.teacher_id) \
        .filter(Student.id == student, Teacher.id == teacher).all()
    print(result)

def sql_12():
    """Оцінки студентів у певній групі з певного предмета на останньому занятті."""

queries_dict = {1:sql_1, 2: sql_2,3:sql_3, 4:sql_4, 5:sql_5, 6:sql_6, 7:sql_7, 8:sql_8, 9:sql_9, 10:sql_10, 11:sql_11}


if __name__ =="__main__":
    while True:
        user_input = input('Choose SQL query: ')
        if user_input == 'exit':
            break
        else:
            try:
                queries_dict.get(int(user_input))()
            except ValueError as err:
                print(f"Incorrect input: {user_input}!!!, Please use integers from 1 to 11")