Introduction
---------------------------
This project was made as a solution to many complaints at my workplace about password requirements being too
difficult to conform to and many, many external blogposts about the different specifications of varying websites.
In response, I created a simple command line password generator that takes password requirements and creates a more
than secure password. It even copies the password to the user's clipboard!

Technologies
---------------------------
All that is used here is Python 3.9.

Setup
---------------------------
Simply run 
```
py -m pip install pypwgen
```
to install! Please run this in a virtual environment. It isn't dangerous; it's just the preferred method of running.

Instructions
---------------------------
# Standard use
First, install the project as stated above. Then, run the main.py in a virtual environment via command line.
You will be prompted for password specifications. If you have none, enter "N" and the generator will create a password
for you using default settings (see Default Settings) and copy it to your clipboard. If not, follow the onscreen prompts
to enter your specifications. Once entered, the password will generate using your specifications as a _minimum_.
Preferrably, the password should be copy / pasted into a password manager because the generator creates extremely complex
passwords that are nearly impossible to memorize. **NEVER** write down passwords and leave them unprotected or store them
in an unecrypted data file. Soon, I will have a password manager available for download, but for now, use a third party
manager.

# Project implementation
This package is not yet compatible with other projects. Please submit a pull request with the correct documentation if you
discover a way to import it!
