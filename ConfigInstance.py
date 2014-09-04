
class ConfigInstance(object):
    def __init__(self, output, values, title="n/a", ):
        self.title = title
        self.values = values
        self.output = output

    def __str__(self):
        return self.title
