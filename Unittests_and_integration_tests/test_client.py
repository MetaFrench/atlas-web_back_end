#!/usr/bin/env python3
"""Test Suite for testing client.py"""
import unittest
from parameterized import parameterized
from unittest.mock import patch
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json', return_value={"name": "test_org"})
    def test_org(self, org_name, mock_get_json):
        github_client = GithubOrgClient(org_name)
        org_info = github_client.org()
        mock_get_json.assert_called_once_with(
            f'https://api.github.com/orgs/{org_name}')
        self.assertEqual(org_info, {"name": "test_org"})


if __name__ == "__main__":
    unittest.main()
