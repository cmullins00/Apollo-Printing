# Apollo-Printing
Apollo Printing capstone group at the University of Idaho.

This repository contains all of the programs that were used to meet the requirements of our capstone project. The Denso programs were run on a RC7M controller in the Wincaps III language, and the Python scripts were run on a Raspberry Pi 4 Model B.

Unfortunately, all of the joint variables that were set on the controller were local and not saved to each program. These program files will not be of much use if you are intending to run them as is, but may provide helpful information about our approach to the problems and how certain commands can be used within the Wincaps III language.

The server.py program is meant to be used with most of the Denso test programs. This python program simply receives messages from the controller, interprets them, and then performs some action utilizing the GPIO pins.

/***********************************************************************************
To have communication between the controller and Pi, the Pi MUST have a static IP address set up for the ethernet port. This can be done by following this tutorial: https://phoenixnap.com/kb/raspberry-pi-static-ip

An ethernet switch is also required to direct the data from one device to another. 
************************************************************************************/

Make sure that the Denso controller has an IP address and port number established in its communication settings. As long as the port number is the same as the port number for the server, it should be able to connect.

If there are any questions or comments, feel free to contact me at connermullins00@gmail.com!
