

class DataSource(object):
    def __init__(self):
        pass

    def __iter__(self):
        return self

    def next(self):
        raise StopIteration
