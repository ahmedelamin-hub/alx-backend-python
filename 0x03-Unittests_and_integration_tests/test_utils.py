#!/usr/bin/env python3
"""
Module for testing access_nested_map function using unittest and parameterized.
"""

import unittest
from parameterized import parameterized
from typing import Any, Dict, Tuple
from utils import access_nested_map

class TestAccessNestedMap(unittest.TestCase):
    """
    TestAccessNestedMap contains test cases for the access_nested_map function.
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

if __name__ == '__main__':
    unittest.main()
