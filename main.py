import random
import string

#Get all characters
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
punctuation = string.punctuation

#Get all characters together
all = lowercase + uppercase + digits + punctuation

#Generate password random
length = int(input())
password = ''.join(random.choice(all) for i in range(length))

#Print password
print(password)
