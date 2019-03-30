class Transaction:
    autocommit: bool

    def __init__(self):
        self.autocommit = True

    def begin(self):
        self.autocommit = False

    def commit(self):
        pass

    def rollback(self):
        pass
