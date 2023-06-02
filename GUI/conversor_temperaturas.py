import tkinter as tk

def converter():
    celsius = float(input_celsius.get())
    fahrenheit = (celsius * 9/5) + 32
    label_resultado.config(text=f'{fahrenheit} ºF')

janela = tk.Tk()
janela.title('Conversor de Temperaturas')

label_instrucao = tk.Label(janela, text='Insira a temperatura em Celsius')
label_instrucao.pack()

input_celsius = tk.Entry(janela)
input_celsius.pack()

btn_converter = tk.Button(janela, text='Converter', command=converter)
btn_converter.pack()

label_resultado = tk.Label(janela, text='')
label_resultado.pack()

janela.mainloop()