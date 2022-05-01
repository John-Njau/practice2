class Source:
    def __init__(self, id, name, description, url):
        self.id = id
        self.name = name
        self.description = description
        self.url = url


class Articles:
    def __init__(self, image, description, time):
        self.image = image
        self.description = description
        self.time = time
