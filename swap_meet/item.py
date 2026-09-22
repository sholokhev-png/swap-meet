import uuid

CONDITION_DESCRIPTION = ["Poor/Non-Functional", "Fair", "Good", "Very Good", "Excellent", "Brand New"]

class Item:
    def __init__(self, id=None, condition=0):
        if id is not None:
            self.id = id
        else:
            new_uuid = uuid.uuid4()
            self.id = new_uuid.int

        self.condition = condition
        
    def get_category(self):
        category = self.__class__.__name__
        return category

    def condition_description(self):
        return CONDITION_DESCRIPTION[self.condition]

    def __str__(self):
        return f"An object of type Item with id {self.id}."
