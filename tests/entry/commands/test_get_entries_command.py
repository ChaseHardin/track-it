import unittest

from entry.commands.get_entries_command import GetEntriesCommand
from tests.entry.entry_data import EntryData


class TestEntriesCommand(unittest.TestCase):
    def test_get_entries__when_multiple_entries_exist(self):
        expected = EntryData().get_multiple_entries()

        actual = GetEntriesCommand().get_entries()

        self.assertEqual(actual, expected)
