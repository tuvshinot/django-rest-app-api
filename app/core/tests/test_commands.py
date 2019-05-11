from unittest.mock import patch

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import TestCase


class CommandsTestCase(TestCase):

    def test_wait_for_db_ready(self):
        """Test waiting for db when db is available"""
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi: # it is default db getting
            gi.return_value = True
            call_command('wait_for_db')
            self.assertEqual(gi.call_count, 1) # this ConnectionHandler calls only once

    @patch('time.sleep', return_value=True)
    def test_wait_for_db(self, ts):
        """Test waiting for db"""
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            gi.side_effect = [OperationalError] * 5 + [True] # 5 times returns error 6th true
            call_command('wait_for_db')
            self.assertEqual(gi.call_count, 6)
