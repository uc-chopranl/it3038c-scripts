
# Hello, Welcome to Neil Chopra's Project 3 for Scripting Language!
-----------------------------------------------------------------
### Project 3: Ceasar Cipher Message Encoder with File Output, Batch Processing, and Randomized Shift-Value

## Overiew
This project is a Ceasar Cipher message encoder with File Output Generation via User Input with Batch Processing capabilities. The user will first be prompted to enter as many messages as they would like to have encoded, each letter in the message(s) will transpose either forward or backward in the alphabet in a specific increment that is generated via the random Python module. 
Once those message(s) are encoded, it will then notify the user that the messages were received. Users will also have the ability to create a backup file which will display both the original and encoded message(s) within a file of their choosing, there will also be an option to just export the encoded message via a file output of the user's choosing.

This is created by creating a list of all of the letters of the alphabet, and running a for loop to have each letter move a random amount of spaces forward from where it was. 
A while loop is also created to further show user input capabilities, as the user can continue encoding messages by simply pressing enter when prompted, or the user can exit out of the program by typing 'quit' when prompted. 
Another while loop is created as well to allow the user to input as many messages as they would like until they break the loop by typing 'done', all of these messages will appear in both your saved text file and your backup text file, there will not be multiple files for multiple messages created.  
 
The script can be run simply through command-line interfaces by locating the directory that the script is located in, and running "python project3.py" which will call the python file within the command line. 

Here is an example of what the script output should look like:

## Script Notes
- Please keep in mind, that the files will be exported to whichever directory you are running the script from, that means if you are running the script from a folder called "python", the generated files will be within that "python" folder. 
- Make sure you include the file extension whenever naming your file.
- This would look like "[file_name].<file_extension>" or "output.txt"


## Example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Example: 

Welcome to the Ceasar Cipher Encoder

Please enter a message to encode (type 'done' to finish): Hello World

Rovvy Gybvn

Message(s) recieved

Please enter a text file name to save your encoded message to (ex: cipher.txt):

cipher.txt

A backup text file will be created containing both your original message and the encoded message, please enter a name for your backup file (ex: backup.txt):

backup.txt

Backup file has been successfully exported to file: backup.txt

Encoded message has been successfully exported to file: cipher.txt

If you would like to quit, please type 'quit', if not, press enter to continue.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Photo Example
![finalprojectcode](https://github.com/uc-chopranl/it3038c-scripts/assets/142918379/9c97387b-96cf-4436-ae34-4339a641f724)
![finalprojectfileoutput](https://github.com/uc-chopranl/it3038c-scripts/assets/142918379/18a1d073-cd62-4940-894e-503be325ea15)
![fp_cipher_output](https://github.com/uc-chopranl/it3038c-scripts/assets/142918379/33ecf2e4-6a53-4f55-acec-8a4d25f463dc)
![fp_backup_output](https://github.com/uc-chopranl/it3038c-scripts/assets/142918379/e093b6d7-319d-442d-9d80-eb9bb3199aef)

## How is this script useful?
This script is very useful in terms of protecting information and encrypting it. Encrypting information provides an extra sense of security, and it will be much harder to figure out any information as you have to decrypt the message to be able to view the contents. This script is also useful as it allows you to encrypt multiple messages, choose the desired file type, as well as being able to output the file with the option for backup as it allows for more customizability and security in case the original file gets corrupted. 

## Source: 

During the creation of this project, I would refer to the GeeksForGeeks page regarding how to encode a message in Python. There were some similarities such as the way that the list was created, although the actual process of converting the original text to an encoded message using a for loop also implementing user input validation through a while loop was originally included in my version of this script and not what GeeksForGeeks had previously. I took some ideas of core fundamentals and coded them in a different way that can work successfully with no errors. I also took some inspiration from W3Schools regarding how to output a file using Python. However, I made some further modifications that would allow user input to generate the type of file they would like to output, providing both a backup and an export option to display said encoded message.

W3Schools "Python File Open" - https://www.w3schools.com/python/python_file_handling.asp

GeeksForGeeks "How to Encode and Decode a Message using Python" - https://www.geeksforgeeks.org/how-to-encode-and-decode-a-message-using-python/
