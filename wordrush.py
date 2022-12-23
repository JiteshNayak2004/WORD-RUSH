from tkinter import *
import time, threading, random
from english_words import english_words_alpha_set
from tkinter import messagebox as mb


class WordleClass():#main class
    def __init__(self):
        self.score = 0
        self.words = []
        self.enteredWords = []
        self.timeLeft = 50

    def start(self):
        self.randomalpha()
        threading.Thread(target=self.trackTime).start()

    def randomalpha(self):#function to display the random list of alphabets
        print("NEW GAME")
        L = [
            'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q',
            'r', 's', 't', 'v', 'w', 'x', 'y', 'z'
        ]
        vowels = ['a', 'e', 'i', 'o', 'u']
        wo = random.sample(vowels, 4)
        o = random.sample(L, 9)
        wo.extend(o)
        self.words = wo
        print(wo)

    def incrementScore(self):#function to increment the score
        self.score += 10

    def countdownGame(self, a):#countdown of the program
        while a > 1:
            a = a - 1
            print(a)
            time.sleep(1)
        print("start")

    def trackTime(self):#main timer of the game
        while self.timeLeft != 0:
            self.timeLeft = self.timeLeft - 1
            time.sleep(1)
        print("Time's up")


root = Tk()
root.title("word race")#title of the game
root.geometry("600x500")#size of the game interface
mylable = Label(root, text="")
mylable.pack(pady="20")
root.configure( bg="cyan")
wordle = WordleClass()

wordle.start()

welcome_msg = '''Welcome Players!!!'''

mb.showinfo('Welcome', welcome_msg)


def program():#function for displaying the list
    anslable.config(text="" ,bg="cyan")
    mylable.config(text=str(wordle.words),bg ='yellow',font=21)


def answer():#this is the main game loop 
    x = ans.get()
    if x not in wordle.enteredWords:
        if x != "" and x in english_words_alpha_set:
            isAllWordsPresent = True
            for i in x:
                if i not in wordle.words:
                    isAllWordsPresent = False
                    break
            if isAllWordsPresent:
                wordle.incrementScore()
                wordle.enteredWords.append(x)
                anslable.config(text="your score is " + str(wordle.score))
                showWarnings.config(text="" , bg="cyan")
            else:
                showWarnings.config(text="Invalid Word", bg="cyan")
        else:
            showWarnings.config(text="Invalid Word", bg="cyan")
    else:
        showWarnings.config(text="This Word is already entered", bg="cyan")
    ans.delete(0, END)

ans = Entry(root, font=("Helvetica", 24))#input box
ans.pack(pady="20")


def delete():#for deleting the input when backspace is pressed
    ans.delete(0, END)


def roll_again():#fucntion to quit the game
    if mb.askyesno("Ask", "Do you wish to quit the game?"):
        mb.showinfo('Thanks', "Thank you for palying")
        root.destroy()


def calculateTimesUp():#function to display the user that the game is over
    while True:
        if not wordle.timeLeft:
            showWarnings.config(text="Times up", bg="cyan")
            delete()



ansbot = Button(root, text="enter", command=answer,bg ='yellow',font= 15)#enter button
ansbot.pack(pady="20")

anslable = Label(root, text="", font=("Helvetica", 18))#displaying the input text
anslable.pack(pady="20")

showWarnings = Label(root, text="", font=("Helvetica", 18),  bg="cyan")#warnings label
showWarnings.pack(pady="10")


threading.Thread(target=calculateTimesUp).start()#program used to run the timer on the background

program()

root.mainloop()#calling the mainloop

