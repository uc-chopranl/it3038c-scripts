#Neil Chopra
#IT3038C - Scripting Language
#Final Project
#Due Date: December 3, 2023

#random module is imported to allow a randomzied value be assiged to the cipher shift. 
import random

print("Welcome to the Caesar Cipher Encoder")

#messages list is created to store user input values
messages = []

while True:
    #while loop is created to allow user to encode as many messages as they want until they type 'done'
    while True:
        #user input to gather messsage(s) to encode	
        user_message = input("Please enter a message to encode (type 'done' to finish): ")       
        
        #User must type done to break the loop, each input is constantly being appended to messages list            
        if user_message.lower() == 'done':
            break
        messages.append(user_message)

    #encoded messages list is created to stored generated encrypted messages
    encoded_messages = []

    for user_message in messages:
        #A random number is generated that will determine the amount of times the message will be shifted
        encoded_message = ""
        shift = random.randint(1, 26)
    
        #list is created for both lowercase and uppercase letters as we will be indexing through this list
        lower_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        upper_alphabet = [letter.upper() for letter in lower_alphabet]

        #for loop is created to take each letter and move it forward in the alphabet dependent on the generated shift
        for letter in user_message:
            if letter in lower_alphabet:
                 encoded_message += lower_alphabet[(lower_alphabet.index(letter) + shift) % 26]
            elif letter in upper_alphabet:
                 encoded_message += upper_alphabet[(upper_alphabet.index(letter) + shift) % 26]
            else:
                 encoded_message+= letter

	#Encrypted messages are appended to encrypted_messages list
        encoded_messages.append(encoded_message)

    print("Message(s) recieved")

    #prompt user for a file name to save the encoded message(s) to
    file_name = input("Please enter a text file name to save your encoded message to (ex: cipher.txt): ")
        
    #prompt user if they would like a backup file containing encoded message(s) and plaintext
    file_backup = input("A backup text file will be created containing both your original message and the encoded message, please enter a name for your backup file (ex: backup.txt): ")

    #export encoded message(s) and plaintext to file backup 
    with open(file_backup, 'w') as file:
        for user_message in messages:
            file.write(user_message + "\n")
        for message in encoded_messages:
            file.write(message + "\n")
    print("Backup file has been successfully exported to file: " + file_backup)
 
    #export encoded message(s) to specified file
    with open(file_name, 'w') as file:
        for message in encoded_messages:
            file.write(message + "\n")

    print("Encoded message has been exported to file: " + file_name)

    #prompt user to continue or exit the program
    print("If you would like to quit type 'quit', if not, press enter to continue.")
    if input() == 'quit':
        break
