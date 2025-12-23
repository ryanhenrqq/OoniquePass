import tkinter as tk

# Parametros da Janela
windowTitle = "OoniquePass - Gerador de senhas"
windowWidth = 1200
windowHeight = 800

root = tk.Tk()
root.title(windowTitle)
root.geometry(f"{windowWidth}x{windowHeight}")
root.resizable(0,0)

headerTitle = tk.Label(root, text=windowTitle, font=("System", 28, "bold"))
headerTitle.pack()

root.mainloop()