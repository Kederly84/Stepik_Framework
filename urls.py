from views import Index, About, InputForm

# Набор адресов как в Django
routes = {
    '/': Index(),
    '/about/': About(),
    '/input/': InputForm()
}
