class Writer:
    def __init__(self, birthday, name, surname, alias, country, works=[], date_death=None):
        self.birthday = birthday
        self.name = name
        self.surname = surname
        self.alias = alias
        self.country = country
        self.works = works
        self.date_death = date_death
    def add_work(self, work):
        self.works.append(work)

class Publisher:
    def __init__(self, name, city):
        self.name = name
        self.city = city

class Work:
    def __init__(self, year, writers=[], publishers=[]):
        self.year = year
        self.writers = writers
        self.publishers = publishers
    def add_writer(self, writer):
        self.writers.append(writer)

class Book(Work):
    def __init__(self, year, binding, cover, writers=[], publishers=[]):
        super().__init__(year, writers, publishers)
        self.binding = binding
        self.cover = cover

class Magazine(Work):
    def __init__(self, year, view, cover, writers=[], publishers=[]):
        super().__init__(year, writers, publishers)
        self.view = view
        self.cover = cover

class Publication(Work):
    def __init__(self, year, place, writers=[], publishers=[]):
        super().__init__(year, writers, publishers)
        self.place = place