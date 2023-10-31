
# Hello, Welcome to Neil Chopra's Project 2 for Scripting Language!
-----------------------------------------------------------------
### Project 2: Ceasar Cipher Message Encoder with File Output 

This project is a Ceasar Cipher message encoder with File Output Generation via User Input. The user will first be prompted to enter a message that they would like to have encoded, each letter in that message will transpose either forward or backward in the alphabet in a specific increment that is generated via the random Python module. 
Once that message is encoded it will then display the newly created cipher message. Users will also have the ability to create a backup file which will display both the original and encoded message within a file of their choosing, there will also be an option to just export the encoded message via a file output of the user's choosing.
Please keep in mind, that the files will be exported to whichever directory you are running the script from, that means if you are running the script from a folder called "python", the generated files will be within that "python" folder. 

This is created by creating a list of all of the letters of the alphabet, and running a for loop to have each letter move a random amount of spaces forward from where it was. 
A while loop is also created to further show user input capabilities, as the user can continue encoding messages by simply pressing enter when prompted, or the user can exit out of the program by typing 'quit' when prompted. 
 
The script can be run simply through command-line interfaces by locating the directory that the script is located in, and running "python project2.py" which will call the python file within the command line. 

Here is an example of what the script output should look like:

## Example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Example: 

Welcome to the Ceaser Cipher Encoder

Please enter a message to encode: Hello World

Rovvy Gybvn

Please enter a text file name to save your encoded message to (ex: cipher.txt):

cipher.txt

A backup text file will be created containing both your original message and the encoded message, please enter a name for your backup file (ex: backup.txt):

backup.txt

Backup file has been successfully exported to file: backup.txt

Encoded message has been successfully exported to file: cipher.txt

If you would like to quit, please type 'quit', if not, press enter to continue.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Photo Example
![project2_output](https://github.com/uc-chopranl/it3038c-scripts/assets/142918379/762229ad-9f03-4ac4-96b7-68a4c3a57fe0)
![file-output-project2](https://github.com/uc-chopranl/it3038c-scripts/assets/142918379/bf3f2d7c-7b34-47d9-bf2b-5efd80a0c06a)
![cipher_output](https://github.com/uc-chopranl/it3038c-scripts/assets/142918379/06c434d8-3b76-400d-8dbf-4fca23cd4ab2)
![backup_output](https://github.com/uc-chopranl/it3038c-scripts/assets/142918379/d9378946-895f-442d-adef-03bc5f51ca64)


During the creation of this project, I would refer to the GeeksForGeeks page regarding how to encode a message in Python. There were some similarities such as the way that the list was created, although the actual process of converting the original text to an encoded message using a for loop also implementing user input validation through a while loop was originally included in my version of this script and not what GeeksForGeeks had previously. I took some ideas of core fundamentals and coded them in a different way that can work successfully with no errors.
I also took some inspiration from W3Schools regarding how to output a file using Python. However, I made some further modifications that would allow user input to generate the type of file they would like to output, providing both a backup and an export option to display said encoded message.


Cited Content: 

W3Schools "Python File Open" - https://www.w3schools.com/python/python_file_handling.asp

GeeksForGeeks "How to Encode and Decode a Message using Python" - https://www.geeksforgeeks.org/how-to-encode-and-decode-a-message-using-python/
