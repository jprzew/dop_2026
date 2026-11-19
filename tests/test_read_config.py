import unittest
from unittest.mock import patch, mock_open

from src.unittest_examples.read_config import read_config

class TestReadConfig(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data='my_result')
    def test_read_config_uses_open(self, mock_file):

         self.assertEqual(read_config('config.ini'), 'my_result')
         mock_file.assert_called_once_with('config.ini')




