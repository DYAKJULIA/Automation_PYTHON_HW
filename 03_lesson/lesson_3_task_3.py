from address import Address
from mailing import Mailing

to_address = Address("101000", "Москва", "Мясницкая", "д. 47", "-")
from_address = Address("123112", "Москва", "Пресненская набережная", "д. 8, стр. 1", "1001 ночь")
cost = 356.38
track = "12311289988786"

mailing = (f"Отправление №{track} из {from_address} в {to_address}. Стоимость {cost} рублей.")

print(mailing)