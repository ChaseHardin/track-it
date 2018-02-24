import unittest

from mock import patch
from entry.services.entry_service import EntryService


class TestSummaryService(unittest.TestCase):
    def setUp(self):
        self.service = EntryService()

    def test_get_entries__when_multiple_entries_exist(self):
        expected = [
            {
                'id': 1,
                'category': 'merge request',
                'summary': 'trying to get people to review'
            },
            {
                'id': 2,
                'category': 'build is down',
                'summary': 'external team broke build'
            }
        ]

        actual = self.service.get_entries()
        self.assertEqual(actual, expected)

    @patch('entry.services.entry_service.GetEntriesCommand.get_entries')
    def test_get_entries__when_no_entries_exist(self, get_entries):
        expected = []
        get_entries.return_value = expected

        actual = self.service.get_entries()

        self.assertEqual(actual, expected)
