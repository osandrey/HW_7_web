
import faker
from random import randint

NUMBER_CLASSES = 6
NUMBER_STUDENTS = 50
NUMBER_GROUPS = 3
NUMBER_TEACHERS = 5
fake_data = faker.Faker('uk_UA')


def generate_fake_data( number_students, number_teachers) -> tuple():
    fake_groups = ['UA1', 'ENG2', 'PL3']  # тут зберігатимемо компанії
    fake_students = []  # тут зберігатимемо співробітників
    fake_classes = ["Math", "Physics", "Philosophy", "History", "Ukrainian language"]
    fake_teachers = []
    # тут зберігатимемо посади
    '''Візьмемо три компанії з faker і помістимо їх у потрібну змінну'''


    # Створимо набір компаній у кількості number_companies
    for _ in range(number_students):
        fake_students.append(fake_data.name())
    # Згенеруємо тепер number_employees кількість співробітників'''
    for _ in range(number_teachers):
        fake_teachers.append(fake_data.name())

    return fake_classes, fake_students,fake_groups, fake_teachers


def prepare_data(classes, students, groups, teachers) -> tuple():
    for_groups = []
    # підготовляємо список кортежів назв компаній
    for gr in groups:
        for_groups.append((gr, ))

    for_students = []  # для таблиці employees

    for student in students:

        for_students.append((student, randint(1, NUMBER_GROUPS)))

    for_teachers = []

    for couch in teachers:

        for_teachers.append((couch, ))

    for_classes = []

    for cl in classes:

        for_classes.append((cl, randint(1, NUMBER_TEACHERS)))

    for_marks = []

    for _ in range(1, 150):

        fake_date = fake_data.date()
        for_marks.append((randint(5, 12), fake_date, randint(1, NUMBER_CLASSES), randint(1, NUMBER_STUDENTS)))


    return for_groups, for_students, for_teachers, for_classes, for_marks



if __name__ == "__main__":
    groups, students, teachers, classes, marks = prepare_data(*generate_fake_data(NUMBER_STUDENTS, NUMBER_TEACHERS))
    print(groups, students, teachers, classes, marks)