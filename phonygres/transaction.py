class Transaction:
    current_schema: str
    autocommit: bool

    def __init__(self):
        self.current_schema = 'public'
        self.autocommit = True

    def begin(self):
        self.autocommit = False

    def commit(self):
        pass

    def rollback(self):
        pass
