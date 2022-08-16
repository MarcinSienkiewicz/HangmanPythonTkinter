import tkinter
import files.game as mainGame
import random
from pathlib import Path
import sqlite3


def selectionWindow():
    root = tkinter.Tk()
    root.resizable(0,0)
    root.title("Difficulty")
    root.iconbitmap("files/icons/question.ico")
    root.config(bg="white", pady=5, padx=5)
    displayHeight = root.winfo_screenheight()
    displayWidth = root.winfo_screenwidth()
    displayHeight = root.winfo_screenheight()
    centeredPosition = f"260x80+{int((displayWidth / 2 - 260 / 2) - 7)}+{int((displayHeight / 2 - 80 / 2) - 36)}"
    root.geometry(centeredPosition)
    root.rowconfigure(index=0, weight=1)
    root.rowconfigure(index=1, weight=1)

    root.columnconfigure(index=1, weight=1)
    root.columnconfigure(index=1, weight=1)
    root.columnconfigure(index=1, weight=1)

    Lselection = tkinter.Label(root, text="Hangman - chose difficulty", bg="white",
                               font=("Code", 14, "bold"), pady=5)
    Lselection.grid(row=0, column=0, columnspan=3, sticky="EW")
    Beasy = tkinter.Button(root, text="Easy", height=2, width=10, bg="#588c7e",
                           fg="white", font=("Code", 9, "bold"), command=lambda: getWord("Easy", root))
    Bmedium = tkinter.Button(root, text="Medium", height=2, width=10, bg="#f2ae72",
                             fg="white", font=("Code", 9, "bold"), command=lambda: getWord("Medium", root))
    Bhard = tkinter.Button(root, text="Hard", height=2, width=10, bg="#d96459",
                           fg="white", font=("Code", 9, "bold"), command=lambda: getWord("Hard", root))

    Beasy.grid(row=1, column=0, sticky="EW")
    Bmedium.grid(row=1, column=1)
    Bhard.grid(row=1, column=2, sticky="EW")

    root.mainloop()

def setUpDb():
    if not Path("files/words.db").exists():
        dbSource = "files/wordsList.txt"

        # minumum word length is 3 characters, words with non-letter chars excluded
        with open(dbSource) as src:
            srcRead = [y for y in (x[:-1].lower()
                         for x in src if len(x[:-1]) > 2) if y.isalpha()]

        # create / connect to the db
        db = sqlite3.connect('files/words.db')
        exec = db.cursor()
        tables = ["Easy", "Medium", "Hard"]

        for table in tables:
            exec.execute("""
            CREATE TABLE IF NOT EXISTS """+table+"""(
            id INTEGER PRIMARY KEY,
            word TEXT);
            """)
        db.commit()

        # popupate the tables accordingly
        idCounters = {"Easy":0, "Medium":0, "Hard":0}
        whichTable = ""
        with db:
            for entry in srcRead:
                if len(entry) < 6:
                    whichTable = "Easy"
                elif len(entry) < 9:
                    whichTable = "Medium"
                else:
                    whichTable = "Hard"

                exec.execute("INSERT INTO "+whichTable+" VALUES(:id, :word)",
                             {'id': idCounters[whichTable], 'word': entry})
                idCounters[whichTable] += 1
        db.close()
    selectionWindow()

def getWord(chosen, root):
    root.destroy()
    db = sqlite3.connect('files/words.db')
    exec = db.cursor()
    exec.execute("SELECT COUNT(*) FROM "+chosen+"")
    tableMax = exec.fetchone()[0]-1
    randomIndex = random.randint(0,tableMax)

    exec.execute("SELECT * FROM "+chosen+" WHERE id=:id;",{'id':randomIndex})
    selectedWord =  exec.fetchone()[1]
    mainGame.makeGui(selectedWord)