#!/usr/bin/env python3
"""
Unit and integration tests for GithubOrgClient.
"""

import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos

class TestGithubOrgClient(unittest.TestCase):
    """
    Test cases for the GithubOrgClient class.
    """

    @parameterized.expand([
        ("google", {"login": "google"}),
        ("abc", {"login": "abc"}),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, expected, mock_get_json):
        """
        Test that GithubOrgClient.org returns the correct value.
        """
        mock_get_json.return_value = expected
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, expected)
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """
        Test the _public_repos_url property.
        """
        mock_org.return_value = {"repos_url": "https://api.github.com/orgs/test/repos"}
        client = GithubOrgClient("test")
        self.assertEqual(client._public_repos_url, "https://api.github.com/orgs/test/repos")

    @patch('client.get_json')
    @patch('client.GithubOrgClient._public_repos_url', new_callable=PropertyMock)
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        """
        Test the public_repos method.
        """
        mock_public_repos_url.return_value = "https://api.github.com/orgs/test/repos"
        mock_get_json.return_value = [
            {"name": "repo1"},
            {"name": "repo2"},
        ]
        client = GithubOrgClient("test")
        self.assertEqual(client.public_repos(), ["repo1", "repo2"])
        mock_get_json.assert_called_once_with("https://api.github.com/orgs/test/repos")
        mock_public_repos_url.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """
        Test the has_license method.
        """
        client = GithubOrgClient("test")
        self.assertEqual(client.has_license(repo, license_key), expected)


@parameterized_class([
    {
        "org_payload": org_payload,
        "repos_payload": repos_payload,
        "expected_repos": expected_repos,
        "apache2_repos": apache2_repos,
    },
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Integration test for the GithubOrgClient.public_repos method.
    """

    @classmethod
    def setUpClass(cls):
        """Set up class by mocking requests.get."""
        cls.get_patcher = patch('requests.get')
        mock_get = cls.get_patcher.start()
        mock_get.return_value.json.side_effect = [
            cls.org_payload, cls.repos_payload
        ]

    @classmethod
    def tearDownClass(cls):
        """Tear down class by stopping the patcher."""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test the public_repos method."""
        client = GithubOrgClient("test")
        self.assertEqual(client.public_repos(), self.expected_repos)
        self.assertEqual(client.public_repos("apache-2.0"), self.apache2_repos)

if __name__ == '__main__':
    unittest.main()
