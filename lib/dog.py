class Dog:
    def _init_(self, name=None, breed=None):
        self._name = None
        self._breed = None

    def name(self):
        return self._name

    
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value
        else:
            print("Name must be a string between 1 and 25 characters.")


    def breed(self):
        return self._breed

    
    def breed(self, value):
        if value in APPROVED_BREEDS:
            self._breed = value
        else:
            print("Breed must be in the list of approved breeds.")

# List of approved dog breeds
APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]