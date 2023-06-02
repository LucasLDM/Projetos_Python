import tkinter as tk

contador = 0

def incrementar():
    global contador
    contador += 1
    label_resultado.config(text=f'{contador}')

janela = tk.Tk()
janela.title('Contador de cliques')
janela.maxsize(200, 100)
janela.minsize(200, 100)

btn_click = tk.Button(text='Incrementar', command=incrementar, font=('Arial', 13))
btn_click.pack(pady=20)

label_resultado = tk.Label(text='')
label_resultado.pack()

janela.mainloop()