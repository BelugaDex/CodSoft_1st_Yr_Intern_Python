from tkinter import *
from PIL import Image, ImageTk
from random import randint

# main window
root = Tk()
root.title("Let's Rock Paper Scissor")
root.config(background="#C14CF7")

# Image importing
rock_img = ImageTk.PhotoImage(Image.open("rock_user.png"))
rock_img_comp = ImageTk.PhotoImage(Image.open("rock.png"))
paper_img = ImageTk.PhotoImage(Image.open("paper_user.png"))
paper_img_comp = ImageTk.PhotoImage(Image.open("paper.png"))
scissor_img = ImageTk.PhotoImage(Image.open("scissors_user.png"))
scissor_img_comp = ImageTk.PhotoImage(Image.open("scissors.png"))

# labelling
user_label = Label(root, image=scissor_img, bg="#C14CF7")
comp_label = Label(root, image=scissor_img_comp, bg="#C14CF7")
comp_label.grid(row=1, column=0)
user_label.grid(row=1, column=4)

# scores
playerScore = Label(root, text=0, font=100, bg="#C14CF7", fg="white")
computerScore = Label(root, text=0, font=100, bg="#C14CF7", fg="white")
computerScore.grid(row=1, column=1)
playerScore.grid(row=1, column=3)

# indicator which side is user or computer
user_indicator = Label(root, font=50, text="User", bg="#C14CF7", fg="white")
comp_indicator = Label(root, font=50, text="Computer",
                       bg="#C14CF7", fg="white")

user_indicator.grid(row=0, column=3)
comp_indicator.grid(row=0, column=1)

# mesages
msg = Label(root, font=50, bg="#C14CF7", fg="white")
msg.grid(row=3, column=2)


# updates messaging part
def updateMessage(x):
    msg['text'] = x


# update user score
def updateUserScore():
    score = int(playerScore["text"])
    score = score + 1
    playerScore["text"] = str(score)


# update computer score
def updateCompScore():
    score = int(computerScore["text"])
    score = score + 1
    computerScore["text"] =str(score)


# check winner
def checkWinner(player, computer):
    if player == computer:
        updateMessage("It's a tie!!!")
    elif player == "rock":
        if computer == "paper":
            updateMessage("You Loose!!!")
            updateCompScore()
        else:
            updateMessage("You Win!!!")
            updateUserScore()
    elif player == "paper":
        if computer == "scissor":
            updateMessage("You Loose!!!")
            updateCompScore()
        else:
            updateMessage("You Win!!!")
            updateUserScore()
    elif player == "scissor":
        if computer == "rock":
            updateMessage("You Loose!!!")
            updateCompScore()
        else:
            updateMessage("You Win!!!")
            updateUserScore()
    else:
        pass


# upadation of choice
choices = ["rock", "paper", "scissor"]


def updateChoice(x):
    # for computer
    compChoice = choices[randint(0, 2)]
    if compChoice == "rock":
        comp_label.configure(image=rock_img_comp)
    elif x == "paper":
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=scissor_img_comp)
    # for user
    if x == "rock":
        user_label.configure(image=rock_img)
    elif x == "paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)
    checkWinner(x, compChoice)


# buttons
rock = Button(root, width=20, height=2, text="ROCK", bg="#FF3E4D", fg="white",
              command=lambda: updateChoice("rock")).grid(row=2, column=1)
paper = Button(root, width=20, height=2, text="PAPER", bg="#FAD02E", fg="white",
               command=lambda: updateChoice("paper")).grid(row=2, column=2)
scissor = Button(root, width=20, height=2, text="SCISSOR", bg="#0ABDE3", fg="white",
                 command=lambda: updateChoice("scissor")).grid(row=2, column=3)

root.mainloop()
