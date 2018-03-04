import unittest

from mock import patch
from entry.services.entry_service import EntryService
from tests.entry.entry_data import EntryData


class TestSummaryService(unittest.TestCase):
    def setUp(self):
        self.service = EntryService()

    def test_get_entries__when_multiple_entries_exist(self):
        expected = EntryData().get_multiple_entries()

        actual = self.service.get_entries()
        self.assertEqual(actual, expected)

    @patch('entry.services.entry_service.GetEntriesCommand.get_entries')
    def test_get_entries__when_no_entries_exist(self, get_entries):
        expected = []
        get_entries.return_value = expected

        actual = self.service.get_entries()

        self.assertEqual(actual, expected)
