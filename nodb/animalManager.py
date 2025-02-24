# Base Animal class
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        return "I make a sound."

# Dog subclass
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")
        self.breed = breed

    def speak(self):
        return "Woof!"


# Cat subclass
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, species="Cat")
        self.color = color

    def speak(self):
        return "Meow!"

# AnimalManager class
class AnimalManager:
    def __init__(self):
        self.animals = []

    def create_default_animals(self):
        """Creates default Dog and Cat objects."""
        self.animals = [
            Dog("Buddy", "Golden Retriever"),
            Cat("Whiskers", "Black")
        ]

    def create_custom_dog(self, name, breed):
        """Creates a custom Dog and adds it to the list."""
        dog = Dog(name, breed)
        self.animals.append(dog)
        return {
            "message": "Dog created successfully!",
            "dog": {
                "name": dog.name,
                "species": dog.species,
                "breed": dog.breed,
                "sound": dog.speak()
            }
        }

    def create_custom_cat(self, name, color):
        """Creates a custom Cat and adds it to the list."""
        cat = Cat(name, color)
        self.animals.append(cat)
        return {
            "message": "Cat created successfully!",
            "cat": {
                "name": cat.name,
                "species": cat.species,
                "color": cat.color,
                "sound": cat.speak()
            }
        }

    def get_dog_json(self):
        """Returns the first Dog’s JSON representation."""
        dog = next((a for a in self.animals if isinstance(a, Dog)), None)
        if dog:
            return {
                "name": dog.name,
                "species": dog.species,
                "breed": dog.breed,
                "sound": dog.speak()
            }
        return {"error": "No dog found."}

    def get_cat_json(self):
        """Returns the first Cat’s JSON representation."""
        cat = next((a for a in self.animals if isinstance(a, Cat)), None)
        if cat:
            return {
                "name": cat.name,
                "species": cat.species,
                "color": cat.color,
                "sound": cat.speak()
            }
        return {"error": "No cat found."}