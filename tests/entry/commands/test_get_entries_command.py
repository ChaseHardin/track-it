import unittest

from entry.commands.get_entries_command import EntryCommand


class TestGetEntriesCommand(unittest.TestCase):
    def test_get_entries_command__when_multiple_entries_exist(self):
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

        actual = EntryCommand.get_entries()

        self.assertEqual(actual, expected)
