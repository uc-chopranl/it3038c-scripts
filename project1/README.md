# Hello, Welcome to Neil Chopra's Project 1 for Scripting Language!
-----------------------------------------------------------------
### Project 1: Ceaser Cipher Message Encoder

This project is a ceaser cipher message encoder. The user will first be prompted to enter a message that they would like to have encoded, each letter in that message will transpose either forward or backward in the alphabet in a specific increment. 
Once that message is encoded it will then display the newly created cipher message. 

This is created by creating a list of all of the letters of the alphabet, and running a for loop to have each letter move 10 spaces forwards from where it was. 
A while loop is also created to further show user input capabilities, as the user can continue encoding messages by simply pressing enter when prompted, or the user can exit out of the program by typing 'quit' when prompted. 
In this case, each letter in the alphabet will be moving forward 10 places, this means if I input the letter 'A', the cipher message output will look like "K".

The script can be run simply through command-line interfaces by locating the directory that the script is located in, and running "python project1.py" which will call the python file within the command line. 

Here is an example of what the script output should look like:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## Example: 

Welcome to the Ceaser Cipher Encoder

Please enter a message to encode: Hello World

Rovvy Gybvn

If you would like to quit, please type 'quit', if not, press enter to continue.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

During the creation of this project, I would refer to the GeeksForGeeks page regarding how to encode a message in Python. There were some similarities such as the way that the list was created, although the actual process of converting the original text to an encoded message using a for loop also implementing user input validation through a while loop was originally included in my version of this script and not what GeeksForGeeks had previously. I took some ideas of core fundamentals and coded them in a different way that can work successfully with no errors.

Citec Content: 

GeeksForGeeks "How to Encode and Decode a Message using Python" - https://www.geeksforgeeks.org/how-to-encode-and-decode-a-message-using-python/
