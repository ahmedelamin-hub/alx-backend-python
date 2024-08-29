#!/usr/bin/env python3
"""
Unit tests for utils functions: access_nested_map, get_json, and memoize.
"""

import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from typing import Any, Dict, Tuple
from utils import access_nested_map, get_json, memoize

class TestAccessNestedMap(unittest.TestCase):
    """
    Test cases for the access_nested_map function.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map: Dict[str, Any], path: Tuple[str, ...], expected: Any) -> None:
        """
        Test that access_nested_map returns the expected output.
        
        Args:
            nested_map (Dict[str, Any]): The nested map to access.
            path (Tuple[str, ...]): The path of keys to follow in the map.
            expected (Any): The expected result from accessing the nested map.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map: Dict[str, Any], path: Tuple[str, ...]) -> None:
        """
        Test that access_nested_map raises a KeyError for invalid paths.
        
        Args:
            nested_map (Dict[str, Any]): The nested map to access.
            path (Tuple[str, ...]): The path of keys to follow in the map.

        Raises:
            KeyError: If the path is not found in the nested map.
        """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), str(path[-1]))

class TestGetJson(unittest.TestCase):
    """
    Test cases for the get_json function.
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url: str, test_payload: Dict[str, Any], mock_get: Mock) -> None:
        """
        Test that get_json returns the expected output and mocks requests.get.

        Args:
            test_url (str): The URL to fetch JSON data from.
            test_payload (Dict[str, Any]): The expected JSON payload.
            mock_get (Mock): The mocked requests.get method.
        """
        mock_get.return_value.json.return_value = test_payload
        response = get_json(test_url)
        mock_get.assert_called_once_with(test_url)
        self.assertEqual(response, test_payload)

class TestMemoize(unittest.TestCase):
    """
    Test cases for the memoize decorator.
    """

    def test_memoize(self) -> None:
        """
        Test that the memoize decorator caches the result of a method.
        """

        class TestClass:
            def a_method(self) -> int:
                return 42

            @memoize
            def a_property(self) -> int:
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as mock_method:
            obj = TestClass()
            self.assertEqual(obj.a_property, 42)
            self.assertEqual(obj.a_property, 42)
            mock_method.assert_called_once()

if __name__ == '__main__':
    unittest.main()
