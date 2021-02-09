from pyowm import OWM
import datetime

owm = OWM('6d15774b8535ecd0755145745cfbc2ef').weather_manager()
weather = owm.weather_at_place('San Diego,CA,US').weather
now = datetime.datetime.now()
print ("Current date and time :")
print (now.strftime("%Y-%m-%d %H:%M:%S"))
print(weather.temperature('fahrenheit'))
