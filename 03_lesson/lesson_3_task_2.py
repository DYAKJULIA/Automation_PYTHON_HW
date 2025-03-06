from smartphone import Smartphone

catalog = [
    Smartphone("HONOR", "Magic7 Pro", "+7 906 732 48 79"),
    Smartphone("Samsung", "Galaxy Z Fold 6", "+7 985 207 03 43"),
    Smartphone("Xiaomi", "15 Ultra", "+7 903 316 60 51"),
    Smartphone("Infinix", "ZERO 30", "+7 929 965 36 06"),
    Smartphone("Iphone", "16 Pro Max", "+7 915 249 52 82")
]

# variation = (f"Марка телефона - {self.brand}, модель телефона - {self.model}, абонентский номер - {self.number}")
#
# print(variation)

for smartphone in catalog:
    print(f"Марка телефона {smartphone.brandPhone} - модель телефона {smartphone.modelPhone}. Абонентский номер: {smartphone.numberPhone}")