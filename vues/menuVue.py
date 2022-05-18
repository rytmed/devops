from curses import window
import tkinter as tk

def showMenu():
    window = tk.Tk()
    window.title('DEVOPS PROJECT')

    """root = tk.Tk()
    frame = tk.Frame(root)
    frame.pack()

    root.title("devops Project")

    w = tk.Label(root, text="Que voulez vous faire ?", fg="red", font=("Arial Bold", 25))
    w.pack()

    button = tk.Button(frame, text="Connexion Routeur/switch", fg="blue", command=connectRouteur)
    button.pack(side=tk.LEFT)

    root.mainloop()"""


def connectRouteur():
    print("youpi cool")
    return True
