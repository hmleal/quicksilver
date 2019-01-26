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


class BaseRequest:
    def __init__(self, environ):
        self._environ = environ

    @property
    def method(self):
        return self._environ["REQUEST_METHOD"]


class BaseResponse:
    # The default charset of the response
    default_charset = "UTF-8"

    def __init__(self, response, status=200, headers=None):
        self.response = response
        if isinstance(self.response, str):
            self.response = response.encode(self.default_charset)

        if headers is None:
            self.headers = [("Content-Type", "text/plain")]
        else:
            self.headers = headers

        self.status = status

    def __call__(self, environ, start_response):
        start_response(self.status_code, self.headers)

        return [self.response]

    @property
    def status_code(self):
        return "{0} {1}".format(self.status, HTTP_STATUS_CODE[self.status].upper())
