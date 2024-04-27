import unittest
from unittest.mock import patch
import requests
from web_crawler import stream_crawl_most_common_words


class TestStreamCrawlMostCommonWords(unittest.TestCase):
    def setUp(self):
        self.url = "http://example.com"

        self.html_content = """
        <html>
            <head><title>Test Page</title></head>
            <body>
                <p>Hello world. This is a test that we test. Testing, one two three.</p>
            </body>
        </html>
        """
        self.expected_words = [('test', 3), ('page', 1), ('hello', 1), ('world', 1), ('this', 1), ('is', 1), ('a', 1), ('that', 1), ('we', 1), ('testing', 1)]

    @patch('requests.get')
    def test_common_words(self, mock_get):
        # Mock the get request to return a fake response
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = self.html_content

        # Test without exclusions
        result = stream_crawl_most_common_words(self.url, num_words=10)
        self.assertEqual(result[0], ('test', 3))  # Check the most common word
        self.assertEqual(len(result), 10)  # Check the number of unique words returned

        # Test with exclusions
        result_with_exclusion = stream_crawl_most_common_words(self.url, num_words=5, exclude=["hello", "test"])

        expected_result = [('page', 1), ('world', 1), ('this', 1), ('is', 1), ('a', 1)]
        self.assertEqual(result_with_exclusion, expected_result)

    @patch('requests.get')
    def test_http_error(self, mock_get):
        # Mock the get request to simulate an HTTP error
        mock_get.return_value.raise_for_status.side_effect = requests.exceptions.HTTPError("404 Client Error: Not Found for url")

        with self.assertRaises(requests.exceptions.HTTPError):
            stream_crawl_most_common_words(self.url)


if __name__ == '__main__':
    unittest.main()