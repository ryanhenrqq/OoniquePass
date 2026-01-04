import tkinter as tk
import random
from tkinter import messagebox

password = []
stripOut = ""
numbLength = 6

# Parametros da Janela
windowTitle = "OoniquePass - Gerador de senhas"
windowWidth = 900
windowHeight = 400

chAmount = "Quantos caracteres deve conter a senha?"
generatedPassword = "Clique em 'Gerar!' para gerar uma senha"

# Componentes
def handleGerar():
    global password
    global numbLength
    global generatedPassword
    global stripOut
    try:
        cha = int(characterAmount.get())
    except ValueError:
        exceptValueError()
        return
    numbLength = cha
    print(cha)
    password = []
    stripOut = ""

    a = 0
    while a < numbLength:
        string = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        print(random.choice(string))
        password.append(random.choice(string))
        a = a+1
    
    b = 0
    bx = ""
    while b < numbLength:
        output = f"{bx}{password[b]}"
        bx = f"{output}"
        b = b+1
    print("Password: ",bx, "\n If you seeing this, the code has worked as well!")
    stripOut = str(bx)
    passOutput["text"] = stripOut

def exceptMainentance():
    mainentanceMessage = "Oops! O item que você executou esta em manutenção, tente novamente mais tarde."
    messagebox.showinfo(windowTitle, mainentanceMessage)


def exceptValueError():
    errorMessage = "Oops! Você precisa digitar um numero válido, tente novamente."
    messagebox.showerror(windowTitle, errorMessage)

# Call inicial do tk
root = tk.Tk()
root.title(windowTitle)
root.geometry(f"{windowWidth}x{windowHeight}")
root.resizable(0,0)

# Elementos
headerTitle = tk.Label(root, text=windowTitle, font=("System", 28, "bold"))
headerTitle.pack()

characterAmountTitle = tk.Label(root, text=chAmount)
characterAmountTitle.pack()
characterAmount = tk.Entry(root)
characterAmount.pack()

generateButton = tk.Button(root, text="Gerar!", command=handleGerar)
generateButton.pack(pady=30)

passOutput = tk.Label(root, text=generatedPassword, font=("System", 22, "bold"))
passOutput.pack()

root.mainloop()