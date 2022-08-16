import tkinter
import files.initialization

def disableRootXButton():
    pass

def finishGame(screen, rootWindow):
    rootWindow.destroy()
    screen.destroy()

def restartGame(screen, rootWindow):
    rootWindow.destroy()
    screen.destroy()

    files.initialization.selectionWindow()

def tryAgain(message, rootWindow):
    screen = tkinter.Tk()
    screen.title("Game Over")
    screen.iconbitmap('files/icons/gameOver.ico')
    displayWidth = screen.winfo_screenwidth()
    displayHeight = screen.winfo_screenheight()
    centeredPosition = f"300x200+{int((displayWidth / 2 - 200 / 2) - 7)}+{int((displayHeight / 2 - 200 / 2) - 36)}"
    screen.geometry(centeredPosition)
    screen.columnconfigure(index=0, weight=1)
    screen.columnconfigure(index=1, weight=1)

    screen.rowconfigure(index=0, weight=1)
    screen.rowconfigure(index=1, weight=1)
    screen.rowconfigure(index=2, weight=1)

    if message[0] == "You won!":
        finishColor = "#9fff80"
        mainColor = "#588c7e"
    else:
        finishColor = "white"
        mainColor = "#d96459"

    screen.configure(bg=mainColor)
    r1 = tkinter.Label(screen, text=message[0], font=("Code", 10, "bold"), bg=mainColor)
    r2 = tkinter.Label(screen, text=message[1], bg=mainColor, font=("Code", 12, "bold"), fg=finishColor)
    another = tkinter.Label(screen, text="Try again?", font=("Code", 18, "bold"), bg=mainColor, fg="white")
    r1.grid(row=0,column=0, sticky="E")
    r2.grid(row=0,column=1, sticky="W")
    another.grid(row=1, column=0, columnspan=2)

    resetButton = tkinter.Button(screen, text="Yes!", command=lambda: restartGame(screen,rootWindow),
                                 font=("Code", 12, "bold"), fg="green", bg="white", width=7)
    resetButton.grid(row=2, column=0, sticky="W", padx=10)


    endGame = tkinter.Button(screen, text="No, quit", command=lambda :finishGame(screen, rootWindow),
                             font=("Code", 12, "bold"), fg="red", bg="white")
    endGame.grid(row=2, column=1, sticky="E", padx=10)
    rootWindow.protocol("WM_DELETE_WINDOW", disableRootXButton)
    screen.protocol("WM_DELETE_WINDOW", lambda :finishGame(screen, rootWindow))
    screen.mainloop()