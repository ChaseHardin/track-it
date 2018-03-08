from tests.entry.entry_data import EntryData


class GetEntriesCommand:

    def __init__(self):
        pass

    @staticmethod
    def get_entries():
        return EntryData().get_multiple_entries()