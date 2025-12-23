import tkinter as tk

# Parametros da Janela
windowTitle = "OoniquePass - Gerador de senhas"
windowWidth = 500
windowHeight = 400

root = tk.Tk()
root.title(windowTitle)
root.geometry(f"{windowWidth}x{windowHeight}")
root.resizable(0,0)

root.mainloop()