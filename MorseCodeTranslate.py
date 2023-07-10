#Morse Code Translator, for purposes of practicing for interviews
#-- Layden Halcomb July 6th, 2023

'''This program takes each letter in the alphabet and translates its corresponding Morse Encryption'''

Morse_Code_Translate = {
                       'A': ".-", 
                       'B': '-...', 
                       'C': '-.-.', 
                       'D': '-..', 
                       'E': '.', 
                       'F': '..-.', 
                       'G':'--.',
                       'H': '....',
                       'I':'..',
                       'J':'.---',
                       'K':'-.-',
                       'L':'.-..',
                       'M':'--',
                       'N':'-.',
                       'O':'---',
                       'P':'.--.',
                       'Q':'--.-',
                       'R':'.-.',
                       'S':'...',
                       'T':'-',
                       'U':'..-',
                       'V':'...-',
                       'W':'.--',
                       'X':'-..-',
                       'Y':'-.--',
                       'Z':'--..',
                    
                       
                       '.': '.-.-.-',
                       ',': '--..--',
                       '?': '..--..',
                       '\'': '. - - - - .',
                       '!': '- . . - -',
                       '/': '- . . - .',
                       ':': '- - - . . .',
                       ';': '- . - . - .',
                       '"': '. - . . - .',
                       '$': '. . . - . . -',
                       '@': '. - - . - .',
                       }


def encrypt(message):
    cipher = ''
    for letter in message: 
        if letter != ' ':
            cipher += Morse_Code_Translate[letter] + ' '
        else: 
            cipher += ' '
    return cipher

def decrypt(message):
    message += ''
    decipher = '' #holds the decrypted sentence in the English alphabet, will return this
    citext = '' # Stores each letter of the Morse code

    for letter in message:

        if letter != ' ':
            i = 0
            citext += letter
        else:
            i += 1

            if i == 2:
                decipher += ' '
            else: 
                for key, value in Morse_Code_Translate.items():
                    if citext == value:
                        decipher += key
                    
                    
                citext = ''
    
    for key, value in Morse_Code_Translate.items():
                    if citext == value:
                        decipher += key
    
    return decipher


if __name__ == "__main__":
   
   MorseCrypt = input("Enter a morse cipher to be decoded:" )
   print(decrypt(MorseCrypt.upper()))
   
   #MorseEncrypt = input("Enter a message to change to morse: ")
   #print(encrypt(MorseEncrypt.upper()))
   


