#!/usr/bin/env python3
"""Test Suite for testing client.py"""
import unittest
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, PropertyMock
from fixtures import TEST_PAYLOAD
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Tests the GithubOrgClient class"""

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Tests whether GithubOrgClient.org returns the correct value"""
        test_client = GithubOrgClient(org_name)
        test_client.org()
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")

    @patch('client.GithubOrgClient.org')
    def test_public_repos_url(self, mock_org):
        """
        Unit-tests the _public_repos_url property of the GithubOrgClient class
        """
        test_payload = {"repos_url":
                        "https://api.github.com/orgs/google/repos"}
        mock_org.return_value = test_payload

        test_client = GithubOrgClient("google")
        result = test_client._public_repos_url

        self.assertEqual(result, test_payload["repos_url"])

    @patch('client.get_json')
    @patch('client.GithubOrgClient._public_repos_url',
           new_callable=PropertyMock)
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        """
        Tests whether the list of repos is what is expected from the chosen
        payload.
        """
        test_payload = [{"name": "repo1"}, {"name": "repo2"}]
        mock_get_json.return_value = test_payload

        mock_public_repos_url.return_value = \
            "https://api.github.com/orgs/google/repos"

        test_client = GithubOrgClient("google")
        result = test_client.public_repos()

        self.assertEqual(result, ["repo1", "repo2"])
        mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """Tests the has_license function from the GithubOrgClient class"""
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)


@parameterized_class([
    {"org_payload": TEST_PAYLOAD[0][0], "repos_payload": TEST_PAYLOAD[0][1],
     "expected_repos": TEST_PAYLOAD[0][2], "apache2_repos": TEST_PAYLOAD[0][3]}
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration testing for public_repos in GithubOrgClient class"""

    @classmethod
    def setUpClass(cls):
        """Method to set up the class for integration testing"""
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        def side_effect(url):
            if url == "https://api.github.com/orgs/google":
                return cls.org_payload
            if url == "https://api.github.com/orgs/google/repos":
                return cls.repos_payload
            return None

        cls.mock_get.side_effect = side_effect

    @classmethod
    def tearDownClass(cls):
        """Method to tear down the class used during integration testing"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Tests repos without license"""
        test_client = GithubOrgClient("google")
        result = test_client.public_repos()
        self.assertEqual(result, self.expected_repos)

    def test_public_repos_with_license(self):
        """Tests repos with license"""
        test_client = GithubOrgClient("google")
        result = test_client.public_repos("apache-2.0")
        self.assertEqual(result, self.apache2_repos)
