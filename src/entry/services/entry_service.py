from src.entry.commands.get_entries_command import GetEntriesCommand


class EntryService:
    def __init__(self):
        pass

    @staticmethod
    def get_entries():
        return GetEntriesCommand().get_entries()
