import unittest
from unittest.mock import patch
from random_quotes import find_quotes_by_author, Quotes,quote_formatter,add_line_breaks

class TestQuoteFunctions(unittest.TestCase):

    def test_quote_formatter_add_line_breaks(self):
        # Mock a quote for testing
        test_quote = "To be or not to be - William Shakespeare"

        # Test the add_line_breaks formatter function
        formatted_quote = quote_formatter(add_line_breaks)(test_quote)

        # Assertions
        self.assertIsInstance(formatted_quote, str)
        self.assertIn("\n", formatted_quote)  # Check if line breaks were added
        self.assertIn("To be or not to be", formatted_quote)
        self.assertIn("William Shakespeare", formatted_quote)

    def test_find_quotes_by_author(self):
        # Ensure the function returns a list
        filtered_quotes = find_quotes_by_author("Mahatma Gandhi")
        self.assertIsInstance(filtered_quotes, list)

        # Ensure all returned quotes contain the author's name
        for quote in filtered_quotes:
            self.assertIn("Mahatma Gandhi", quote)

        # Ensure the function handles case-insensitivity
        filtered_quotes_upper = find_quotes_by_author("MAHATMA GANDHI")
        self.assertEqual(filtered_quotes, filtered_quotes_upper)

if __name__ == '__main__':
    unittest.main()


