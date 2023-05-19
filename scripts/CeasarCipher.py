print('''                                               
 .d8888b 8888b.  .d88b. .d8888b  8888b. 888d888 
d88P"       "88bd8P  Y8b88K         "88b888P"   
888     .d88888888888888"Y8888b..d888888888     
Y88b.   888  888Y8b.         X88888  888888     
 "Y8888P"Y888888 "Y8888  88888P'"Y888888888   ''')
print('''                                           
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88                                             ''')

purpose = ''
while not(purpose.lower() == 'decrypt') and not(purpose.lower() == 'encrypt'):
    purpose = input("Enter 'Encode' to encrypt or 'Decode' to decrypt: ")
key = int(input("Enter key: "))
word = input("Enter phrase, word or sentence: ")
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']
wordList = []
finalList = []
encryptedString = ""
for i in word:
    wordList.append(i.lower())
if purpose.lower() == 'encrypt':
    for i in range(len(wordList)):
        if wordList[i] != " ":
            position = key + (alphabets.index(wordList[i]))
            if position < len(alphabets):
                finalList.append(alphabets[position])
            else:
                position = position - 26
                finalList.append(alphabets[position])
        else:
            finalList.append(" ")
    for i in finalList:
        encryptedString = encryptedString + i
    print(f"Ceaser cipher encrypts to : '{encryptedString}'")
else:
    for i in range(len(wordList)):
        if wordList[i] != " ":
            position = (alphabets.index(wordList[i])) - key
            if position > -1:
                finalList.append(alphabets[position])
            else:
                position = position + 26
                finalList.append(alphabets[position])
        else:
            finalList.append(" ")
    for i in finalList:
        encryptedString = encryptedString + i
    print(f"Ceaser cipher decrypts to : '{encryptedString}'")