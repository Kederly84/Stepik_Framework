import time


class Route:

    def __init__(self, url: str, routes: dict = None):
        self.url = url
        if routes is None:
            routes = {}
        self.routes = routes

    def __call__(self, cls):
        self.routes[self.url] = cls()


class Debug:

    def __init__(self, name, debug: bool = True):
        self.name = name
        self.debug = debug

    def __call__(self, cls):
        def wrapper(func):
            def profiling(*args, **kwargs):
                if self.debug:
                    time_start = time.time()
                    res = func(*args, **kwargs)
                    time_end = time.time()
                    time_length = time_end - time_start
                    print(f'{self.name} completed in {time_length:2.2f} ms')
                else:
                    res = func(*args, **kwargs)

                return res

            return profiling

        return wrapper(cls)
