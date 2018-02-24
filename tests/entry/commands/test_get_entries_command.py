import unittest

from entry.commands.get_entries_command import GetEntriesCommand


class TestEntriesCommand(unittest.TestCase):
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

        actual = GetEntriesCommand().get_entries()

        self.assertEqual(actual, expected)
