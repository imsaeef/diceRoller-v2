from tkinter import *
from PIL import Image, ImageTk
import random
import pygame

root = Tk()
root.title("Dice roller V2")
root.geometry("400x300+450+50")
root.config(bg="#005977")
root.resizable(0, 0)


#die faces import
dices = [
    "d1.png",
    "d2.png",
    "d3.png",
    "d4.png",
    "d5.png",
    "d6.png"
]

#show image
showImg = ImageTk.PhotoImage(file="d6.png")
label = Label(root, bd=0, bg="#005977", image=showImg)
label.place(x=150, y=100, height=100, width=100)

#initialize pygame
pygame.mixer.init()
#rolling dices
def rolling():
    #load sound
    pygame.mixer.music.load("dice.mp3")
    #play sound
    pygame.mixer.music.play(loops=0)
    #logic
    dieImg = ImageTk.PhotoImage(Image.open(random.choice(dices)))
    label.config(image=dieImg)
    label.Image = dieImg

#button
button = Button(root, font="exo 15 bold", text="Roll Dice", bg="#0091c0", activebackground="#0091c0", fg="#ffffff", activeforeground="#ffffff", bd=2, relief="raised", cursor="hand2", command=rolling)
button.place(x=150, y=230, width=100, height=30)

#tag name
label1 = Label(root, text="Dice rolling by SAEEF", font="exo 10 bold", bd=0, fg="#005977", bg="#ffffff")
label1.place(x=0, y=20, width=400)

root.mainloop()