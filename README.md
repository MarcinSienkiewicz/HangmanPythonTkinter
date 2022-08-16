# Hangman #

### Running the game ###
`python hangman.pyw`

### About ###
Classic hangman game. You've got six attempts to guess an English word.
There are three levels of difficulty - the higher the difficulty the longer the word:
- **Easy** 3-5 letters
- **Medium** 6-7 letter
- **Hard** 8-14 letters

The words are saved in the **sqlite3** database ('cause why not) and randomly chosen from there depending on selected difficylty.
There are **2,958** words in the database in total and all are lowercase letters only (non letter characters are not accepted as input, uppercase transformed to lower case).

If there are multiple occurrences of a letter in the word, only the *first* occurrence will be uncovered per guess.
#### Requirements ####
- Python (using tkinter) with Pillow module (to be able to view my expertly drawn paint images).

``` python -m pip install Pillow```