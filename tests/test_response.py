import unittest

from quicksilver.http import BaseResponse as Response


class TestResponse(unittest.TestCase):
    def test_response_as_string(self):
        resp = Response("Hello world!")

        self.assertEqual(b"Hello world!", resp.response)

    def test_status_code_ok(self):
        resp = Response("Hello world!", status=200)

        self.assertEqual(resp.status_code, "200 OK")

    def test_status_code_not_found(self):
        resp = Response("Hello world!", status=404)

        self.assertEqual(resp.status_code, "404 NOT FOUND")

    def test_empty_headers(self):
        resp = Response("Empty headers")

        self.assertEqual(resp.headers, [("Content-Type", "text/plain")])

    def test_json_headers(self):
        headers = [("Content-Type", "application/json")]
        resp = Response("Json headers", headers=headers)

        self.assertEqual(resp.headers, headers)
