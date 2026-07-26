## More comprehensions
# Task 3 (Price difference of cheaper properties)


class RealProperty:
    def __init__(self, rooms: int, square_metres: int, price_per_sqm: int,description):
        self.rooms = rooms
        self.square_metres = square_metres
        self.price_per_sqm = price_per_sqm
        self.description = description

    def bigger(self, compared_to):
        if self.square_metres > compared_to.square_metres:
            return True
        else:
            return False
    def price_difference(self, compared_to):
        final1 = self.square_metres * self.price_per_sqm
        final2 = compared_to.square_metres * compared_to.price_per_sqm
        if final1 > final2 :
            return final1 - final2
        else:
            return final2 - final1

    def more_expensive(self, compared_to):
        final1 = self.square_metres * self.price_per_sqm
        final2 = compared_to.square_metres * compared_to.price_per_sqm
        if final1 > final2 :
            return True
        else:
            return False

def cheaper_properties(properties: list, reference: RealProperty):
    return [i for i in properties if reference.more_expensive(i) == True]


a1 = RealProperty(1, 16, 5500, "Central studio")
a2 = RealProperty(2, 38, 4200, "Two bedrooms downtown")
a3 = RealProperty(3, 78, 2500, "Three bedrooms in the suburbs")
a4 = RealProperty(6, 215, 500, "Farm in the middle of nowhere")
a5 = RealProperty(4, 105, 1700, "Loft in a small town")
a6 = RealProperty(25, 1200, 2500, "Countryside mansion")

properties = [a1, a2, a3, a4, a5, a6]

print(f"cheaper options when compared to {a3.description}:")
for item in cheaper_properties(properties, a3):
    print(f"{item.description:35} price difference {item.price_difference(a3)} euros")
