# Quicksilver

Another Python handmade web framework

## Getting Started

```Please don't use this in production```

I've created this only to learn how to create a web framework from scratch.

### Example

```python
from quicksilver import Application
from quicksilver.http import BaseResponse as Response
from quicksilver.http import Route

def home():
  return Response(b"home")


routes = (
  Route("/", home, name="home"),
)


app = Application(routes=routes)


if __name__ == "__main__":
  from wsgiref.simple_server import make_server
  
  server = make_server("127.0.0.1", 8000, app)
  server.serve_forever()
```
