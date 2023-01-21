from views import Index, About, InputForm, CoursesList, CategoriesList

# Набор адресов как в Django
routes = {
    '/': Index(),
    '/about/': About(),
    '/input/': InputForm(),
    '/courses-list/': CoursesList(),
    '/categories-list/': CategoriesList()
}
