# Quicksilver

Another Python handmade web framework

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

## Getting Started

```Please don't use this in production```

I've created this only to learn how to create a web framework from scratch.

### Example

```python

from quicksilver import Application
from quicksilver.http import BaseResponse as Response
from quicksilver.http import Route


def home(request):
    return Response("method: {0}".format(request.method))


def news(request, pk, slug):
    return Response("Params: {0} - {1}".format(pk, slug))


routes = (
    Route(r"^$", handler=home),
    Route(r"^news/(?P<pk>\d+)/(?P<slug>[-\w]+)/$", handler=news),
)

app = Application(routes=routes)


if __name__ == "__main__":
  from wsgiref.simple_server import make_server

  server = make_server("127.0.0.1", 8000, app)
  server.serve_forever()

```
