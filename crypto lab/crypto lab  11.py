#vigenere cipher
plaintext=input("ENter plaintext:\t")
keyword=input('enter keyword:\t')
plaintext=plaintext.upper()
keyword=keyword.upper()
def generatekey(plaintext,key):
    key=list(key)
    if len(plaintext)==len(key):
        return(key)
    else:
        for i in range(len(plaintext)-len(key)):
            key.append(key[i%len(key)])
        return ("" . join(key))
key=generatekey(plaintext,keyword)
print(key)
def encrypt_function(plaintext):
    cipher=""
    for i in range(len(plaintext)):
        if plaintext[i]==" ":
            cipher+=" "
        else:
            cipher+=chr((ord(plaintext[i])+ord(key[i])-65)%26+65)
    return cipher
print("cipher  text:"   +encrypt_function(plaintext))
ciphertext=encrypt_function(plaintext)
def  decrypt_function(ciphertext):
    originalmessage=""
    for i in range(len(ciphertext)):
        if ciphertext[i]==" ":
            originalmessage+=" "
        else:
            originalmessage+=chr((ord(ciphertext[i])-ord(key[i])-65)%26+65)
    return originalmessage
print("original  text:"   +decrypt_function(ciphertext))
    

