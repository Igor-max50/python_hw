from address import Address
from mailing import Mailing

to_address = Address("индекс: 176098", "г.Тверь", "ул.Абрикосовая", "д.100", "кв.50")
from_address = Address("индекс: 147360", "г.Тула", "ул.Виноградная", "д.12", "кв.145")

mailing = Mailing(to_address, from_address, 1000, "D13711")

print(f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, "
      f"{mailing.from_address.street} {mailing.from_address.house} - {mailing.from_address.apartment} "
      f"в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street} "
      f"{mailing.to_address.house} - {mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")