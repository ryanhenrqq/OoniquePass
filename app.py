import tkinter as tk
import random
from tkinter import messagebox

# Strings globais essenciais
password = []
stripOut = ""
numbLength = 6

# Parametros da Janela & strings
programName = "Oonique Pass"
windowTitle = f"{programName} - Gerador de senhas"
windowWidth = 900
windowHeight = 400

class App:
    def __init__(self):
        self.minAmount = 6 # minimo de caracteres da senha
        self.maxAmount = 30 # maximo de caracteres
        self.chAmount = f"Quantos caracteres deve conter a senha (entre {self.minAmount} a {self.maxAmount})?"
        self.generatedPassword = "Clique em 'Gerar!' para gerar uma senha"

        self.root = tk.Tk()
        self.root.title(windowTitle)
        self.root.geometry(f"{windowWidth}x{windowHeight}")
        self.root.resizable(0,0)

        # Elementos
        self.headerTitle = tk.Label(self.root, text=windowTitle, font=("System", 28, "bold"))
        self.headerTitle.pack()

        self.characterAmountTitle = tk.Label(self.root, text=self.chAmount)
        self.characterAmountTitle.pack()
        self.characterAmount = tk.Entry(self.root)
        self.characterAmount.pack()

        self.generateButton = tk.Button(self.root, text="Gerar!", command=self.handleGerar)  # ideia posterior: timer de cooldown para cada geração de senha diferente
        self.generateButton.pack(pady=30)

        self.passOutput = tk.Label(self.root, text=self.generatedPassword, font=("System", 22, "bold"))
        self.passOutput.pack()
    

    def handleGerar(self):
        global password # array necessaria
        global numbLength # quantidade desejada pelo usuario
        global stripOut # str onde a senha vai ficar no final
        try:
            cha = int(self.characterAmount.get()) 
        except ValueError:
            self.exceptValueError()
            return
        if cha < self.minAmount or cha > self.maxAmount:
            self.exceptValueError()
            return
        numbLength = cha
        print(cha)
        password = []
        stripOut = ""

        # separar o codigo abaixo em uma funçao separada
        a = 0
        while a < numbLength:
            string = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
            print(random.choice(string)) # debug temporario, remover dps!
            password.append(random.choice(string))
            a = a+1
        # ^^^

        b = 0
        bx = ""
        while b < numbLength:
            if not b == 0:
                output = f"{bx}{password[b]}"
                bx = f"{output}"
            else:
                output = f"{password[b]}" # retrabalho: corrigir white space no inicio da string, essa solução
                bx = f"{output}"          # não funcionou
            b = b+1
        # separar o codigo abaixo em uma função separada
        print("Password: ",bx, "\n If you seeing this, the code has worked as well!")
        stripOut = str(bx)
        self.passOutput["text"] = stripOut
    

    # handlers especiais globais
    # ideia posterior: separa as strings abaixo em uma parte apenas para as strings do codigo, para treinar melhor a organização e codigo limpo
    def exceptMainentance(self):
        mainentanceMessage = "Oops! O item que você executou esta em manutenção, tente novamente mais tarde."
        messagebox.showinfo(windowTitle, mainentanceMessage)

    def exceptValueError(self):
        errorMessage = "Oops! Você precisa digitar um numero válido, tente novamente."
        messagebox.showerror(windowTitle, errorMessage)
    
    def run(self):
        self.root.mainloop()