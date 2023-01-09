#shift cipher
plaintext=input("ENter plaintext:\t")
s=int(input('enter number of shifts:\t'))
plaintext=plaintext.upper()
def encrypt_function(plaintext):
    cipher=""
    for i in range(len(plaintext)):
        if plaintext[i]==" ":
            cipher+=" "
        else:
            cipher+=chr((ord(plaintext[i])+s-65)%26+65)
    return cipher
print("cipher  text:"   +encrypt_function(plaintext))
ciphertext=encrypt_function(plaintext)
def  decrypt_function(ciphertext):
    originalmessage=""
    for i in range(len(ciphertext)):
        if ciphertext[i]==" ":
            originalmessage+=" "
        else:
            originalmessage+=chr((ord(ciphertext[i])-s-65)%26+65)
    return originalmessage
print("original  text:"   +decrypt_function(ciphertext))
    
