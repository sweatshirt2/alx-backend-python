from unittest import TestCase
from unittest.mock import patch, MagicMock
from parameterized import parameterized
from utils import access_nested_map, get_json


class TestAccessNestedMap(TestCase):

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(self, nested_map, path, expected):
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected)

    @parameterized.expand([({}, ("a")), ({"a": 1}, ("a", "b"))])
    def test_access_nested_map_exception(self, nested_map, path):
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(TestCase):
    # @parameterized.expand(
    #     [
    #         ("http://example.com", {"payload": True}),
    #         ("http://holberton.io", {"payload": False}),
    #     ]
    # )
    # @patch("get")
    # def test_get_json(self, test_url, test_payload):
    #     pass

    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]
    )
    def test_get_json(self, test_url, test_payload):
        with patch("requests.get") as mock_requests_get:
            # Todo: fix this to make it a response object with the payload returned from rs.json()
            mock_response = MagicMock()
            mock_response.status_code = 200
            mock_response.json.return_value = test_payload

            mock_requests_get.return_value = mock_response
            self.assertEqual(get_json(test_url), test_payload)
