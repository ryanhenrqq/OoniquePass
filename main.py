import tkinter as tk
from tkinter import messagebox

# Parametros da Janela
windowTitle = "OoniquePass - Gerador de senhas"
windowWidth = 900
windowHeight = 400

chAmount = "Quantos caracteres deve conter a senha?"
generatedPassword = "Clique em 'Gerar!' para gerar uma senha"

# Componentes
def handleGerar():
    exceptMainentance()


def exceptMainentance():
    mainentanceMessage = "Oops! O item que você executou esta em manutenção, tente novamente mais tarde."
    messagebox.showinfo(windowTitle, mainentanceMessage)

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