import quopri


class Person:

    def __init__(self, name: str, age: int, email: str, is_active: bool = True, deleted: bool = False):
        self.name = name
        self.age = age
        self.email = email
        self.is_active = is_active
        self.deleted = deleted

    def __str__(self):
        return f'Это {self.name},возраст {self.age} лет, почта {self.email}. ' \
               f'Объект создан в классе {self.__class__.__name__}'


class Teacher(Person):
    pass


class Student(Person):
    pass


class PersonFactory:
    types = {
        'Teacher': Teacher,
        'student': Student
    }

    @classmethod
    def create(cls, type_of_person: str, name: str, age: int, email: str, is_active: bool = True,
               deleted: bool = False):
        return cls.types[type_of_person](name, age, email, is_active, deleted)


class Category:
    auto_id = 0

    def __init__(self, name: str):
        self.pk = Category.auto_id
        Category.auto_id += 1
        self.name = name
        self.courses = []

    def course_count(self):
        result = len(self.courses)
        return result


class Course:

    def __init__(self, name: str, category: Category):
        self.name = name
        self.category = category
        self.category.courses.append(self)

    def __str__(self):
        return f'Курс {self.name} в категории {self.category}. Объект создан в классе {self.__class__.__name__}'


class VerbinarCourse(Course):
    pass


class RecordCourse(Course):
    pass


class CoursesFactory:
    types = {
        'verbinar': VerbinarCourse,
        'record': RecordCourse
    }

    @classmethod
    def create(cls, type_of_course: str, name: str, category: Category):
        return cls.types[type_of_course](name, category)


class Engine:
    def __init__(self):
        self.teachers = []
        self.students = []
        self.courses = []
        self.categories = []

    @staticmethod
    def create_user(type_of_person: str, name: str, age: int, email: str, is_active: bool = True,
                    deleted: bool = False):
        return PersonFactory.create(type_of_person, name, age, email, is_active, deleted)

    @staticmethod
    def create_category(name: str):
        return Category(name)

    def find_category_by_id(self, pk):
        for item in self.categories:
            print('item', item.pk)
            if item.pk == pk:
                return item
        raise Exception(f'Нет категории с id = {pk}')

    def find_category_by_name(self, name: str):
        for item in self.categories:
            if item.name == name:
                return name
            else:
                return None

    @staticmethod
    def create_course(type_of_course: str, name: str, category: Category):
        return CoursesFactory.create(type_of_course, name, category)

    def get_course(self, name):
        for item in self.courses:
            if item.name == name:
                return item
        return None

    @staticmethod
    def decode_value(val):
        val_b = bytes(val.replace('%', '=').replace("+", " "), 'UTF-8')
        val_decode_str = quopri.decodestring(val_b)
        return val_decode_str.decode('UTF-8')


class SingletonByName(type):

    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls.__instance = {}

    def __call__(cls, *args, **kwargs):
        if args:
            name = args[0]
        elif kwargs:
            name = kwargs['name']
        if name in cls.__instance:
            return cls.__instance[name]
        else:
            cls.__instance[name] = super().__call__(*args, **kwargs)
            return cls.__instance[name]


class Logger(metaclass=SingletonByName):

    def __init__(self, name):
        self.name = name

    @staticmethod
    def log(text):
        print('log--->', text)
