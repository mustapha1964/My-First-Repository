# # This little program provides all possible 4 digits pascodes 

# from string import digits
# from itertools import product

# for passcode in product(digits, repeat=4):
#      print("".join(passcode))

# # This little program provides all possible 4 (digits & letters) passcode

# from string import ascii_letters
# from itertools import product

# for passcode in product(ascii_letters, repeat=4):
#      print("".join(passcode))


# This little program provides all possible 4 caracters passcode 

# from string import ascii_letters, digits, punctuation
# from itertools import product

# for passcode in product(ascii_letters + digits + punctuation, repeat=4):
#      print("".join(passcode))  

# This little program provides all possible 4 ponctuations passcode 

from string import  punctuation
from itertools import product

for passcode in product(punctuation, repeat=4):
     print("".join(passcode))  