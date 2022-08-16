from pathlib import Path
from PIL import ImageTk, Image
import tkinter
import files.gameOver as gOver

def makeGui(selectedWord):
    windowColor = "#5E7D7E"
    movesLeft = [6]
    originalWord = selectedWord
    selectedWord = list(selectedWord)

    # word to be guessed - we don't want to see this
    # print("".join(selectedWord))

    guessMe = ["_" for x in range(len(selectedWord))]

    def verify():
        letterGiven = inputLetter.get().lower()
        inputLetter.delete(0, tkinter.END)

        # input checks
        if len(letterGiven) == 0 or ord(letterGiven) < 97 or ord(letterGiven) > 122:
            return

        # word check
        if letterGiven in selectedWord:
            foundIndex = selectedWord.index(letterGiven)
            guessMe[foundIndex] = letterGiven
            selectedWord[foundIndex] = "*"
            guess.config(text = guessMe)

        else:
            movesLeft[0] -= 1
            valueLabel.configure(text=movesLeft)

            # display updated image
            path = f"files/img/{6-movesLeft[0]}.png"
            updatedImage = ImageTk.PhotoImage(Image.open(path))
            imageLabel.configure(image=updatedImage)

            # below line prevents garbage collection - retains new image when exiting this function
            # if not added - no image will be displayed as when returning to makeGUI new image
            # will be discarded
            imageLabel.image = updatedImage

        # end game check
        endGame = ""
        if movesLeft[0] == 0:
            endGame = "lost"
            endColor="red"
            endMessage = ["You lost, correct answer:",originalWord]
        elif guessMe.count("_")==0:
            endGame = "won"
            endMessage = ["You won!", "Congratulations"]
            endColor="#9fff80"

        if endGame != "":
            statusLabel.configure(text="You", fg=endColor)
            valueLabel.configure(text=f"{endGame}!", fg=endColor)
            checkButton.configure(state=tkinter.DISABLED)
            inputLetter.configure(state=tkinter.DISABLED)
            # call play again window - root still active at this point!
            gOver.tryAgain(endMessage, root)


    # game window
    root = tkinter.Tk()
    root.resizable(0,0)
    root.columnconfigure(index=0, weight=1)
    root.columnconfigure(index=1, weight=1)
    root.title("Hangman")
    root.iconbitmap("files/icons/game.ico")
    displayWidth = root.winfo_screenwidth()
    displayHeight = root.winfo_screenheight()
    centeredPosition = f"400x500+{int((displayWidth / 2 - 400 / 2) - 7)}+{int((displayHeight / 2 - 500 / 2) - 36)}"
    root.geometry(centeredPosition)
    root.configure(bg=windowColor, padx=5, pady=5)

    outerFrame = tkinter.Frame(root, bg=windowColor)
    outerFrame.grid(row=0, column=0, columnspan=2, sticky="NSEW")
    outerFrame.columnconfigure(index=0, weight=1)
    outerFrame.columnconfigure(index=1, weight=1)

    outerFrame.rowconfigure(index=0, weight=1)
    outerFrame.rowconfigure(index=1, weight=1)
    outerFrame.rowconfigure(index=2, weight=1)
    outerFrame.rowconfigure(index=3, weight=1)

    statusLabel = tkinter.Label(outerFrame, text="Moves left:", bg=windowColor, fg="white",
                                font=("Code",15,"bold"),pady=10)
    valueLabel = tkinter.Label(outerFrame, text=movesLeft, bg=windowColor, fg="#9fff80", font=("Code", 15, "bold"))
    statusLabel.grid(row=0, column=0,sticky=tkinter.E)
    valueLabel.grid(row=0, column=1, sticky=tkinter.W)

    # image
    # pngs 0.png ... 5.png; lost.png and 7.png (winner img)
    currentImage = ImageTk.PhotoImage(Image.open(f"files/img/{6 - movesLeft[0]}.png"))
    imageLabel = tkinter.Label(outerFrame, image=currentImage)
    imageLabel.grid(row=1, column=0,columnspan=2)

    # word to guess
    hidden = "_"*len(selectedWord)
    guess = tkinter.Label(outerFrame, text=guessMe, bg=windowColor, fg="white",
                          font=("Code", 15, "bold"), pady=15)

    guess.grid(row=2, column=0,columnspan=2)
    inputLabel = tkinter.Label(outerFrame, text="Letter:", bg=windowColor, fg="white", font=("Code", 11, "bold"),
                               padx=5)

    # input letter; max one character validation
    def maxOneLetter(*args):
        value = playerEntered.get()
        if len(value) > 1: playerEntered.set(value[:1])

    playerEntered = tkinter.StringVar()
    playerEntered.trace('w', maxOneLetter)

    inputLabel.grid(row=3, column=0, sticky=tkinter.E)
    inputLetter = tkinter.Entry(outerFrame, bg="white",fg="black", font=("Code", 15, "bold"),
                                width=2, justify="center", textvariable=playerEntered)

    inputLetter.grid(row=3, column=1, sticky=tkinter.W, pady=10)
    checkButton = tkinter.Button(outerFrame, text="Check Letter", width=20, border=1,
                                 command=lambda: verify())
    checkButton.grid(row=4,column=0,columnspan=2)

    root.mainloop()