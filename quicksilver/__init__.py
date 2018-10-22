from quicksilver.http import BaseResponse as Response


class Application:
    def __call__(self, environ, start_response):
        response = index()

        return response(environ, start_response)


app = Application()


def index():
    return Response(b"My first page")