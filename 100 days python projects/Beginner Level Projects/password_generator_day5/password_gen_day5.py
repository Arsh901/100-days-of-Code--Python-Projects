
letter =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
import random
print("Welcome to the PyPassword Generator.")
l = int(input("How many letters would you like in your password?\n"))
n = int(input("How many numbers would you like?\n"))
s = int(input("How many symbols would you like?\n"))
lisl = []
lisn = []
liss = []
for i in range(0,l):
    a = random.choice(letter)
    lisl.append(a)
for i in range(0,n):
    b = random.choice(numbers)
    lisn.append(b)
for i in range(0,s):
    c = random.choice(symbols) 
    liss.append(c)
f = lisl+lisn+liss
print(f)
# password with definite pattern 👇
pass_with_pattern = ""  
for i in range(0,l+n+s):
    pass_with_pattern += f[i] 
print("A password with pattern will be: "+pass_with_pattern)
# password with definite pattern ☝️

# password without definite pattern 👇
random.shuffle(f)
pass_without_pattern = ""
for i in range(0,l+s+n):
    pass_without_pattern +=f[i]
print("A password without pattern will be: "+pass_without_pattern)















