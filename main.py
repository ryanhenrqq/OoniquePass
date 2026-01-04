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

minAmount = 6 # minimo de caracteres da senha
maxAmount = 30 # maximo de caracteres
chAmount = f"Quantos caracteres deve conter a senha (entre {minAmount} a {maxAmount})?"
generatedPassword = "Clique em 'Gerar!' para gerar uma senha"

# Componentes
def handleGerar():
    global password # array necessaria
    global numbLength # quantidade desejada pelo usuario
    global stripOut # str onde a senha vai ficar no final
    try:
        cha = int(characterAmount.get()) 
    except ValueError:
        exceptValueError()
        return
    if cha < minAmount or cha > maxAmount:
        exceptValueError()
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
    passOutput["text"] = stripOut

# handlers especiais globais
# ideia posterior: separa as strings abaixo em uma parte apenas para as strings do codigo, para treinar melhor a organização e codigo limpo
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

generateButton = tk.Button(root, text="Gerar!", command=handleGerar)  # ideia posterior: timer de cooldown para cada geração de senha diferente
generateButton.pack(pady=30)

passOutput = tk.Label(root, text=generatedPassword, font=("System", 22, "bold"))
passOutput.pack()

# ideia posterior (dependendo do caminho q o codigo seguir): historico das senhas geradas em um arquivo encriptado
root.mainloop()