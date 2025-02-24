import json

from noapi import Dog, Cat


# AnimalManager class
class AnimalManager:
    def __init__(self):
        self.animals = []

    def __create_animals(self):
        """Private method to create Dog and Cat objects and count animals."""
        dog = Dog("Buddy", "Golden Retriever")
        cat = Cat("Whiskers", "Black")
        self.animals.extend([dog, cat])
        print(f"Number of animals created: {len(self.animals)}")

    def __dog_to_json(self, dog):
        """Private method to convert Dog object to JSON."""
        dog_data = {
            "name": dog.name,
            "species": dog.species,
            "breed": dog.breed,
            "sound": dog.speak()
        }
        return json.dumps(dog_data, indent=4)

    def display_dog_json(self):
        """Public method to display dog JSON."""
        self.__create_animals()
        dog = next((a for a in self.animals if isinstance(a, Dog)), None)
        if dog:
            dog_json = self.__dog_to_json(dog)
            print("Dog JSON Representation:")
            print(dog_json)
        else:
            print("No dog found.")