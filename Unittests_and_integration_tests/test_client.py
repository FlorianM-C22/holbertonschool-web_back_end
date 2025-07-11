#!/usr/bin/env python3
"""Test client module.
"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test class for GithubOrgClient class."""

    @parameterized.expand([
        ("google", {"login": "google"}),
        ("abc", {"login": "abc"}),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, expected_repos, mock_get_json):
        """Test GithubOrgClient.org method."""
        mock_get_json.return_value = expected_repos
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, expected_repos)
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")
