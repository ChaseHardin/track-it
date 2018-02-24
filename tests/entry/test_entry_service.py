import unittest

from entry.entry_service import Entry


class TestSummaryService(unittest.TestCase):
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

        actual = Entry.get_entries()

        self.assertEqual(actual, expected)
