class EntryService:
    def __init__(self, entry_command):
        self.entry_command = entry_command

    def get_entries(self):
        return self.entry_command.get_entries()
