class EntryData:

    def __init__(self):
        pass

    @staticmethod
    def get_multiple_entries():
        return [
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