class Rolex:
    chapati_size: str
    num_eggs: int
    # toppings: bool = False
    toppings: []
    with_salt: bool = True

    def __int__(self, chapati_size: str, num_eggs: int, toppings, ):
        self.chapati_size = chapati_size
        self.num_eggs = num_eggs
        self.toppings = toppings

    # def price(self, tax: float):

    def __repr__(self):
        return f"Rolex toppings are: {', '.join(self.toppings)}"


rolex = Rolex("large", 3, ["tomatoes", "cabbage", "Onions"])  # there is an issue here to consult and find out what is
# wrong
print(rolex)


# Inheritance:
class SpecialRolex(Rolex):
    def __init__(self, toppings, extra_toppings):
        super().__init__("large", 3, toppings)

    def __repr__(self):
        return f"Special Rolex with toppings are: {', '.join(self.toppings)}, " \
               f"and extra toppings: {', '.join(self.extra_toppings)}"


specialRolex = SpecialRolex(["tomatoes", "cabbage"], ["cheese", "onions", "sukumaweek"])
print(specialRolex)


# Polymorphism:
def rolexPoly(rolex):
    print(rolex)


rolexPoly(rolex)
rolexPoly(specialRolex)

# Encapsulation 💊💊
"""--> wrapping the data and functions inside the object. no one should access them from the outside. 
this can be similar to private and public in Java.
We utilize the getters and setters.
"""


class Rolexx:
    def __init__(self, toppings):
        self.__toppings = toppings

    def __repr__(self):
        return f"Rolexx toppings are: {', '.join(self.toppings)}"

    # getter
    def get_toppings(self):
        return self.__toppings

        # setter

    def set_toppings(self, toppings):
        return self.__toppings.append(toppings)


rolexx = Rolexx(["tomatoes", "onions"])
# print(rolexx)

print(rolexx.get_toppings())

rolexx.set_toppings("sukuma week")
print(rolexx)


# Abstraction
class Rolexz:
    def __init__(self, toppings):
        self.toppings = toppings

    def __repr__(self):
        return f"Rolexz toppings are: {', '.join(self.toppings)}"


rolexz = Rolexz(["onions", "cheese", "tomatoes"])
print(rolexz)

# Overloading / Overriding
class Rolexz:
    def __init__(self, toppings):
        self.toppings = toppings

    def __repr__(self):
        return f"Rolexz toppings are: {', '.join(self.toppings)}"