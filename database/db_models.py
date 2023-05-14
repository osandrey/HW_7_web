from sqlalchemy import Column, Integer, String, ForeignKey, Date, func
from .db_conn import Base
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property

# Таблиця студентів;
# Таблиця груп;
# Таблиця викладачів;
# Таблиця предметів із вказівкою викладача, який читає предмет;
# Таблиця де кожен студент має оцінки з предметів із зазначенням коли оцінку отримано;


class Teacher(Base):
    """id INTEGER PRIMARY KEY AUTOINCREMENT,
    fullname VARCHAR(100) UNIQUE NOT NULL"""
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50))
    last_name = Column(String(50))

    @hybrid_property
    def full_name(self):
        return f"{self.first_name}{self.last_name}"

class Group(Base):
    """id INTEGER PRIMARY KEY AUTOINCREMENT,
       group_name VARCHAR(100)  NOT NULL"""
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True, autoincrement=True)
    group_name = Column(String(6), unique=True)


class Student(Base):
    """id INTEGER PRIMARY KEY AUTOINCREMENT,
    fullname VARCHAR(100)  NOT NULL,
    group_id REFERENCES groups (id)
      ON DELETE CASCADE
      ON UPDATE CASCADE"""
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    group_id = Column(Integer, ForeignKey('groups.id', ondelete='CASCADE'))
    groups = relationship('Group', backref='students')
    @hybrid_property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

class Class(Base):
    """id INTEGER PRIMARY KEY AUTOINCREMENT,
    class_name VARCHAR(100) UNIQUE NOT NULL,
    teacher_id REFERENCES teachers (id)"""
    __tablename__ = 'classes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    class_name = Column(String(50), unique=True)
    # teacher_name = Column(String(50))
    teacher_id = Column(Integer, ForeignKey('teachers.id', ondelete='CASCADE'))
    teacher = relationship('Teacher', backref='classes')



class Mark(Base):
    """id INTEGER PRIMARY KEY AUTOINCREMENT,
    mark INTEGER,
    date_of DATE NOT NULL,
    class_id REFERENCES classes (id),
    student_id REFERENCES students (id)"""
    __tablename__ = 'marks'
    id = Column(Integer, primary_key=True, autoincrement=True)
    # student_name = Column(String(50))
    mark = Column(Integer)
    date = Column(Date, default=func.now())
    student_id = Column(Integer, ForeignKey('students.id', ondelete='CASCADE'))
    students = relationship('Student', backref='marks')
    class_id = Column(Integer, ForeignKey('classes.id', ondelete='CASCADE'))
    classes = relationship('Class', backref='marks')




