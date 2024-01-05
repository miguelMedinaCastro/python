import random 

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
special = "!@#$%*()[]{}\|,.;:?/°º=-_+'"
num = "0123456789" 

all = lower + upper + special + num 
length = 20 
password = "".join(random.sample(all, length)) 

print(password)
