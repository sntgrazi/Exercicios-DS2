from person import Person

class PersonFactory():
    def __init__(self) -> None:
        self.id = 0

    def create_person(self, name, age):
        self.id += 1
        
        return Person(self.id-1, name, age)