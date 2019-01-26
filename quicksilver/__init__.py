import re

from quicksilver.http import BaseRequest as Request
from quicksilver.http import BaseResponse as Response


class Application:
    def __init__(self, routes=None):
        self.routes = routes

    def __call__(self, environ, start_response):
        request = Request(environ)

        for route in self.routes:
            route_match = re.match(route.pattern, environ["PATH_INFO"][1:])

            if route_match:
                response = route.handler(request, **route_match.groupdict())

                return response(environ, start_response)

        response = Response("Page not Found", status=404)

        return response(environ, start_response)
