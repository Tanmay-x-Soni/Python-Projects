#Ceaser Cipher project
alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]


def encoding(orignal_value , shifting_value):
    encoded_value=""
    
    for letter in orignal_value:
        if letter not in alphabet:
            encoded_value += letter
        else:
            shifted_position = alphabet.index(letter) + shifting_value
        

            if shifted_position > len(alphabet)-1:
                shifted_position = shifted_position - len(alphabet)
       
        #or
        # shifted_position %= len(alphabet)
        
            encoded_value += alphabet[shifted_position]
    
    print(f"\nHere is the encoded value : {encoded_value}")

def decoding(encoded_value , shifting_value):
    decoded_value = ""

    for letter in encoded_value:
        if letter not in alphabet:
            decoded_value += letter
        else:
            shifted_position = alphabet.index(letter) - shifting_value

            decoded_value += alphabet[shifted_position]
    
    
    print(f"\nHere is the decoded value : {decoded_value}")

        
print('''
                                                                  
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88         


           88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88                                             
 
''')

process = True 
while(process == True ):

    operation = int(input("Enter the operation to be performed ! \n   '0' for encrypting , '1' for decrypting. \n"))
    
    if operation == 0:
        encode = input("Enter code to encode  : ").lower()
        shift_value = int(input("Enter shift value : \n"))
        encoding(orignal_value=encode ,shifting_value= shift_value)
    elif operation == 1 :
        decode = input("Enter code to decode  : ").lower()
        shift_value = int(input("Enter shift value : \n"))
        decoding(encoded_value=decode ,shifting_value= shift_value)
    else:
        print("Invalid operation , Stopping process! ")
        break    

    
    retry= input("Wanna continue or abort the operation ? \n  Type 'yes' for continue  & 'no' for exit. \n ").lower()

    if retry == 'yes':
        process==True
    elif retry == 'no':
        process == False
    else:
        print("Invalid operation , Stopping process! ")
        break    
    
    

