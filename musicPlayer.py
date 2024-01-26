"""
Program: musicPlayer.py
1/11/2024

Simple Command-Line based music player app that can play a standard .mp3 audio file.

*** MUST INSTALL the pygame package before running this app!!!

At command prompt run: pip install pygame --pre
"""

# Import statement for the pygame mixer module
from pygame import mixer

# Initialize the mixer module
mixer.init()

# Display a menu for the user interface
print("\nWelcome to the Python Music Player!")
print("Enter 1 to SELECT a song file.")
print("Enter 2 to PLAY the chosen song.")
print("Enter 3 to PAUSE an active song.")
print("Enter 4 to UNPAUSE the song.")
print("Press any other key to exit the program.")

# Logic statements that determine which options to enter and what to do with the commands.
while True:
    menuChoice = input("Please enter a menu option >> ")

    # Decision making that triggers each feature
    if menuChoice == "1":
        songFile = input("Please enter the song's filename >> ")
        mixer.music.load(songFile)
    elif menuChoice == "2":
        mixer.music.play()
    elif menuChoice == "3":
        mixer.music.pause()
    elif menuChoice == "4":
        mixer.music.unpause()
    else:
        input("Thank you for using the music player!! Press ENTER to exit >> ")
        break

    




