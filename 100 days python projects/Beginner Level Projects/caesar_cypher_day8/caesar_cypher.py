import art
print(art.logo) 
l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = str(input("Type 'encode' to encrypt or 'decode' to decrypt: \n"))
message = str(input("Enter your message:\n"))
s = int(input("Type the shift number: "))
s = s%26
def encode(m):
    m = m.lower()
    m = list(m)
    n= 0
    for i in m:
        if i in l:
            indl = l.index(i)
            m[n] = l[indl+s]
            n = n+1 
        else:
            m[n]= m[n]
            n=n+1
    m = ''.join(m)
    print(f"The encoded expression formed by {s} shifts is : {m}")
        
def decode(m):
    m = m.lower()
    m = list(m)
    n= 0
    for i in m:
        if i in l:
            indl = l.index(i)
            m[n] = l[indl- s]
            n = n+1 
        else:
            m[n]= m[n]
            n=n+1
    m = ''.join(m)
    print(f"The decoded expression formed by {s} shifts is : {m}")

if direction == "encode":
    encode(m = message)
else:
    decode(m = message)
    

    

