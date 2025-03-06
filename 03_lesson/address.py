class Address:

    def __init__(self, index, sity, street, house, apartment):
        self.index = index
        self.sity = sity
        self.street = street
        self.house = house
        self.apartment = apartment

    def __str__(self):                                             #отправление
        return (f"{self.index}, {self.sity}, {self.street}, {self.house}, {self.apartment}")