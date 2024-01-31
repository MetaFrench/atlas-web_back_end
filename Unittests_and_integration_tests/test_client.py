#!/usr/bin/env python3
"""Test Suite for testing client.py"""
import unittest
from parameterized import parameterized
from unittest.mock import patch, PropertyMock
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

    @patch('client.GithubOrgClient.org', return_value={"repos_url": "https://api.github.com/orgs/test_org/repos"})
    def test_public_repos_url(self, mock_org):
        github_client = GithubOrgClient("test_org")

        # Mock the memoized property
        with patch.object(GithubOrgClient, '_public_repos_url', new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = "https://api.github.com/orgs/test_org/repos"

            # Call the method and assert the result
            result = github_client._public_repos_url
            self.assertEqual(
                result, "https://api.github.com/orgs/test_org/repos")


if __name__ == "__main__":
    unittest.main()
