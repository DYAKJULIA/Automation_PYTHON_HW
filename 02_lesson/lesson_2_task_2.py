year = int(input("Введите год: "))

def is_year_leap(year):
     if year % 4 == 0:
          print(f"Год {year}: True")
     else:
          print(f"Год {year}: False")

is_year_leap(year)