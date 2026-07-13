import pyjokes
import pyttsx3

joke = pyjokes.get_joke()
print(joke)
print("hello!")

engine = pyttsx3.init()
engine.say("Mitali how are u???")
engine.runAndWait()

import os

# Specify the directory path
path = "."

# Print all files and folders in the directory
contents = os.listdir(path)

print("Contents of the directory:")
for item in contents:
    print(item)