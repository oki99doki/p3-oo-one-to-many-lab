
class Pet:

    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    all = []

    def __init__(self, name, pet_type, owner = None):
        self.name = name
        if pet_type in Pet.PET_TYPES:
            self.pet_type = pet_type
        else:
            raise Exception("Pet ist not from the list")
        self.owner = owner
        Pet.all.append(self)

class Owner:

    def __init__(self, name):
        self.name = name
    
    def add_pet(self, pet):
        if isinstance(pet,Pet):
            pet.owner = self
        else:
            raise Exception("This pet is not ...")

    # Pet needs to be method. e.g. for pet in Pet.all , do ...
    def pets(self):
        this_owners_pets = []
        for cur_pet in Pet.all:
            if cur_pet.owner == self:
                this_owners_pets.append(cur_pet)
        return this_owners_pets

    def get_sorted_pets(self):
        sorted_pets = sorted(self.pets(), key=lambda pet: pet.name)
        return sorted_pets
