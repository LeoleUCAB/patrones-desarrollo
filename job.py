class Job:
    def __init__(self, name, pages):
        self.name = name
        self.pages = pages

    def __str__(self):
        return '{} ({} pages)'.format(self.name, self.pages)