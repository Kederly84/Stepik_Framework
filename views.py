from framework.templator import render

from patterns.creation_patterns import Engine, Logger

site = Engine()
logger = Logger('main')


class Index:

    def __call__(self, requests):
        return '200 OK', render('index.html')


class About:

    def __call__(self, requests):
        return '200 OK', render('about.html')


class InputForm:

    def __call__(self, requests):
        return '200 OK', render('input.html')


class CoursesList:
    def __call__(self, request):
        logger.log('Список курсов')
        if request['method'] == 'POST':
            data = request['data']
            name = data['coursename']
            name = site.decode_value(name)
            category_id = data['category']
            course_type = data['courseType']
            if category_id and name and course_type:
                category = site.find_category_by_id(int(category_id))
                course = site.create_course(course_type, name, category)
                site.courses.append(course)
        courses = site.courses
        object_list = []
        for course in courses:
            obj = {'name': course.name, 'category': course.category.name, 'category_id': course.category.pk}
            if course.__class__.__name__ == 'VerbinarCourse':
                obj['course_type'] = 'Вербинарный формат'
            else:
                obj['course_type'] = 'Курс в записи'
            object_list.append(obj)
        categories = site.categories
        categories_list = []
        for cat in categories:
            cat_obj = {'id': cat.pk, 'name': cat.name}
            categories_list.append(cat_obj)
        return '200 OK', render('courses.html', objects=object_list, categories=categories_list)


class CategoriesList:

    def __call__(self, request):
        logger.log('Список категорий')
        if request['method'] == 'POST':
            data = request['data']
            name = data['categoryname']
            name = site.decode_value(name)
            category = site.find_category_by_name(name)
            if not category:
                new_category = site.create_category(name)
                site.categories.append(new_category)
        categories = site.categories
        object_list = []
        for cat in categories:
            obj = {'name': cat.name, 'id': cat.pk}
            object_list.append(obj)

        return '200 OK', render('categories.html', objects=object_list)
