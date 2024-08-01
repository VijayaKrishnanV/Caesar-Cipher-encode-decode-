alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
from art import logo
print(logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
shift=shift%26
encode=[]
decode=[]

value=True
def encrypt(text, shift):
    blank=[]
    blank=alphabet[shift:]+alphabet[:shift]
    for i in range(len(text)):
        for j in range(len(alphabet)):
            if text[i]==alphabet[j]:
                encode.append(blank[j])
        if text[i] not in alphabet:
            encode.append(text[i])
    output="".join(encode)
    print(output)

def decrypt(text, shift):
    blank=[]
    blank=alphabet[shift:]+alphabet[:shift]
    for i in range(len(text)):
        for j in range(len(alphabet)):
            if text[i]==blank[j]:
                decode.append(alphabet[j])
        if text[i] not in blank:
            decode.append(text[i])
    output="".join(decode)
    print(output)

while value==True:  

    if direction=="encode":
        encrypt(text, shift)
    elif direction=="decode":
        decrypt(text, shift)
    n=str(input("Do u want to continue? Y OR N\n")).lower()
    if n=="y":
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        shift=shift%26
    elif n=="n":
        value=False
    else:
        print("Enter y or n correctly\n")

