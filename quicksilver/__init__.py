from quicksilver.http import BaseResponse as Response


class Application:
    def __init__(self, routes=None):
        self.routes = routes

    def __call__(self, environ, start_response):
        for r in self.routes:
            if r.path == environ["PATH_INFO"]:
                response = r.handler()
                return response(environ, start_response)

        response = Response(b"Page not Found", status=404)
        return response(environ, start_response)
