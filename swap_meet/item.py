import uuid

class Item:
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            new_uuid = uuid.uuid4()
            self.id = new_uuid.int
        
    def get_category(self):
        category = self.__class__.__name__
        return category

    def __str__(self):
        return f"An object of type Item with id {self.id}."
