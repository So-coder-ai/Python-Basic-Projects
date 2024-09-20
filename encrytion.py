import random
import string
char=" "+string.punctuation+string.ascii_letters+string.digits
char=list(char)
key =char.copy()
random.shuffle(key)
print(f"char :{char}")
print()
print(f"key :{key}")
#encryption
v1=input("enter the input in plain text ")
v1=list(v1)
cypher=""
for letter in v1:
    index=char.index(letter)
    cypher+=key[index]
 
print(f"your cyphered text is {cypher}")
#decryption
cypher_text=input("enter the input in plain text ")
cypher_text=list(cypher_text)
plain=""
for letter in cypher_text:
    index=key.index(letter)
    plain+=char[index]
 
print(f"your plain text is {plain}")

