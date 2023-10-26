#Neil Chopra
#IT3038C - Scripting Language
#Project 2 - Ceaser Cipher Encoder with File Output and Shift-Value
#Due Date: October 29, 2023

import random
print("Welcome to the Ceaser Cipher Encoder")
#while loop is created to allow user to encode as many messages as they want until they type 'quit'
while True:
    #user input to gather messsage to encode	
    user_message = input("please enter a message to encode: ")
    encoded_message = ""

    #A random number is generated that will determine the amount of times the message will be shifted
    shift = random.randint(1, 26)

    #list is created for both lowercase and uppercase letters as we will be indexing through this list
    lower_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    upper_alphabet = [letter.upper() for letter in lower_alphabet]

    #for loop is created to take each letter and move it 10 places forward in the alphabet
    for letter in user_message:
        if letter in lower_alphabet:
             encoded_message += lower_alphabet[(lower_alphabet.index(letter) + shift) % 26]
        elif letter in upper_alphabet:
             encoded_message += upper_alphabet[(upper_alphabet.index(letter) + shift) % 26]
        else:
             encoded_message+= letter
    else:
        print(encoded_message)

        #prompt user for a file name to save the encoded message to
        file_name = input("Please enter a file name to save your encoded message to (ex: cipher.txt): ")
  
        #export message to specified file
        with open(file_name, 'w') as file:
            file.write(encoded_message)
        print("Encoded message has been exported to file: " + file_name)

        #prompt user to continue or exit the program
        print("If you would like to quit type 'quit', if not, press enter to continue.")
        if input() == 'quit':
            break