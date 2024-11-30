class Rectangle:

    def __init__(self, length, width, color="red"):
        self.length = length
        self.width = width
        self.color = color
    
    def volume(self):
        return self.width * self.length

    def __str__(self) -> str:
        return f"Rectangle de longueur {self.length}, largeur {self.width}, couleur {self.color}"

rectangle = Rectangle(5, 3)
print(f"Aire du rectangle : {rectangle.volume()}")

class Cake:

    def __init__(self, flavor):
        self.flavor = flavor

    def cut(self):
        if (self.flavor == "chocolat"):
            return f"couper le gateau au {self.flavor} en 4"
        elif (self.flavor == "banane"):
            return f"couper le gateau à la {self.flavor} en 4"
        else:
            return f"couper le gateau en 4"
    
gateau_au_chocolat = Cake(flavor="chocolat")
gateau_a_la_banane = Cake(flavor="banane")
print(vars(gateau_a_la_banane))

print(f"Le chocolat : {gateau_au_chocolat.flavor}, la banane : {gateau_a_la_banane.flavor}")
print(gateau_a_la_banane.cut())

class Bird:
    """Les attributs définis ici sont des attributs de classe."""
    names = ('mouette', 'pigeon', 'moineau', 'hirrondelle')
    positions = {}

    def __init__(self, name):
        """Les attributs définis ici sont des attributs d'instance."""
        self.position = 1, 2
        self.name = name
        self.positions[self.position] = self.name
    
    @classmethod
    def find_bird(cls, position):
        """Retrouve un oiseau selon la position donnée."""
        if position in cls.positions:
            return f"On a trouvé un {cls.positions[position]}"

        return "On a rien trouvé"
    
    @staticmethod
    def get_def():
        """Donne la définition d'un oiseau"""
        return ("Animal (vertébré à sang chaud) au corps recouvert de plumes,"
                "dont les membres antérieurs sont des ailes et qui a un bec")

Bird.names
Bird.positions
print(Bird.find_bird((2,5)))

bird = Bird("mouette")
print(Bird.find_bird((1,2)))

print(Bird.get_def())