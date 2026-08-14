from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

# Change language

from pyowm.owm import OWM
from pyowm.utils.config import get_default_config
config_dict = get_default_config()
config_dict['language'] = 'ru'  # your language here, eg. Portuguese

owm = OWM('YOUR_API_KEY')
mgr = owm.weather_manager()

print("Узнайте погоду и время в своём городе")
place = input('В каком городе/стране?: ')

observation = mgr.weather_at_place(place)
w = observation.weather

print('В городе ' + place + ' сейчас ' + w.detailed_status)

temp = w.temperature('celsius') ['temp']
print('Температура сейчас в районе: ' + str(temp))

if temp < 5:
	print('Сейчас ппц как холодно, одевайся как танк!')
elif temp < 20:
	print('Сейчас холодно, оденься потеплее.')
else:
	print('Температура норм, одевай что угодно.')