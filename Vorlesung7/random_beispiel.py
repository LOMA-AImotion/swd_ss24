import random
from random import randint
# lokales, selbstdefiniertes Modul
import thi_swd

#random.seed(1337)
x = random.randint(0, 10)
y = randint(0, 100)
print(f"x = {x}")
print(f"y = {y}")
print(random.choice("NSWE"))

thi_swd.greet()
print(thi_swd.my_double(15.0))