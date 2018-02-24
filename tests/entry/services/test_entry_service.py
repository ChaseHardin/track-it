import unittest

from mock import create_autospec

from entry.commands.get_entries_command import EntryCommand
from entry.services.entry_service import EntryService


class TestEntryService(unittest.TestCase):

    def setUp(self):
        self.command_mock = create_autospec(EntryCommand)

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

        self.command_mock.get_entries.return_value = expected
        entry_service = EntryService(self.command_mock)

        actual = entry_service.get_entries()

        self.assertEqual(actual, expected)

    def test_get_entries__when_no_entries_exist(self):
        expected = []
        self.command_mock.get_entries.return_value = expected
        entry_service = EntryService(self.command_mock)

        actual = entry_service.get_entries()

        self.assertEqual(actual, expected)
