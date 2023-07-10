#Ceasar Cipher Encryption and Decryption

def encrypt(key,message):
    message = message.upper()
    alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for letter in message:
        if letter in alph:
            num = (alph.find(letter) + key)%len(alph)
            result+= alph[num]
        else: 
            result+=letter
    return result

def decrypt(key, message):
    message = message.upper()
    alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for letter in message: 
        if letter in alph:
            num = (alph.find(letter) - key)%len(alph) #finding the corresponding letter in the alphabet to decipher
            result += alph[num]
        else: 
            result+=letter
    return result 

if __name__ == "__main__":
    print(decrypt(3, "Khoor dqg zhofrph wr wkh zruog ri idhuxq. D pdjlfdo odqg ri zlwfkhv, zlcdugv dqg gudjrqv. Duh brx suhsduhg iru dq dgyhqwxuh zkhuh brx duh wdvnhg zlwk wkh prvw gdqjhurxv wdvn, Uxqqlqj d sdqgd hasuhvv nlwfkhq"))

    print(encrypt(3, "I dont like you talking to me in Morse"))