import datetime
from datetime import timedelta, date
import my_module_math
from colorama import Fore, init

print(datetime.date.today())
print(datetime.timedelta(minutes=70))

print(date.today())
print(timedelta(minutes=70))

my_module_math.add(30, 80)
my_module_math.substract(80, 30)

init(convert=True)
print(Fore.RED + "Hello world")
