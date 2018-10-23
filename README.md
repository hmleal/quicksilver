# Quicksilver

Another Python handmade web framework

## Getting Started

```Please don't use this in production```

I've created this only to learn how to create a web framework from scratch.

### Example

```python
from quicksilver import Application


app = Application()


if __name__ == "__main__":
  from wsgiref.simple_server import make_server
  
  server = make_server("127.0.0.1", 8000, app)
  server.serve_forever()
```
