HTTP_STATUS_CODE = {
    200: "OK",
    301: "Moved Permanently",
    302: "Found",
    404: "Not Found",
    500: "Internal Server Error",
}


class Route:
    def __init__(self, pattern, handler, name=None):
        self.pattern = pattern
        self.handler = handler
        self.name = name


class BaseResponse:
    def __init__(self, response=None, status=200):
        if response is None:
            self.response = []
        else:
            self.response = response

        self.status = status

    def __call__(self, environ, start_response):
        start_response(self.status_code, [("Content-Type", "text/plain")])

        return [self.response]

    @property
    def status_code(self):
        return "{0} {1}".format(self.status, HTTP_STATUS_CODE[self.status].upper())
