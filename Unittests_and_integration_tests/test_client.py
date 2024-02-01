#!/usr/bin/env python3
"""Test Suite for testing client.py"""
import unittest
from parameterized import parameterized
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):

    @patch('client.get_json', return_value={"name": "test_org"})
    def test_org(self, mock_get_json):
        github_client = GithubOrgClient("test_org")
        org_info = github_client.org()
        mock_get_json.assert_called_once_with(
            f'https://api.github.com/orgs/test_org')
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

    @patch('client.GithubOrgClient._public_repos_url', return_value="https://api.github.com/orgs/test_org/repos")
    @patch('client.get_json', return_value=[{"name": "repo1"}, {"name": "repo2"}])
    def test_public_repos(self, mock_get_json, mock_public_repos_url):
        github_client = GithubOrgClient("test_org")

        # Call the method and assert the result
        repos = github_client.public_repos()
        expected_repos = [{"name": "repo1"}, {"name": "repo2"}]

        # Assert that the mocks were called once
        mock_get_json.assert_called_once_with(
            "https://api.github.com/orgs/test_org/repos")
        mock_public_repos_url.assert_called_once()

        # Assert the result
        self.assertEqual(repos, expected_repos)


if __name__ == "__main__":
    unittest.main()
