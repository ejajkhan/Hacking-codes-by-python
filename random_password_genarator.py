import string
from random import *
character=string.ascii_letters+string.digits
password="".join(choice(character) for x in range(1,15))
print("",password)
