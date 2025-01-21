import tkinter as tk

class Calculadora:

    def __init__(self, root):
        self.root = root
        self.root.title('Calculadora POO')
        self.root.configure(bg='#2b3e50')

        self.pantalla = tk.Entry(self.root, width=60, bg='#3b4b5b', borderwidth=8, fg='white')
        self.pantalla.grid(row=0, column=0, padx=10, pady=15, columnspan=4)

        self.crear_botones()

    def crear_botones(self):
        botones = [
            ('1', 1, 0), ('2', 1, 1), ('3', 1, 2),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
            ('7', 3, 0), ('8', 3, 1), ('9', 3, 2),
            ('0', 4, 0), ('+', 1, 3), ('-', 2, 3),
            ('*', 3, 3), ('/', 4, 3), ('=', 4, 1),
            ('C', 4, 2), 
        ]

        for (contenido, fila, columna) in botones:
            boton = tk.Button(self.root, text=contenido, bg='#4b5b6b', fg='white', padx=35, pady=35,
                                command=lambda texto=contenido: self.boton_click(texto))

            boton.grid(row=fila, column=columna)

    def boton_click(self, valorCapturado):
        if valorCapturado == '=':

            expresion = self.pantalla.get()

            if not expresion.strip():
                self.pantalla.delete(0, tk.END)
            else:
                try:
                    resultado = str(eval(expresion))
                    self.pantalla.delete(0, tk.END)
                    self.pantalla.insert(0, resultado)
                except :
                    self.pantalla.delete(0, tk.END)
                    self.pantalla.insert(0, 'Error: No fue posible hacer el calculo')
        elif valorCapturado == 'C':
            self.pantalla.delete(0, tk.END)
        else:
            valorActual = self.pantalla.get()
            self.pantalla.delete(0, tk.END)
            self.pantalla.insert(0, valorActual + valorCapturado)



root = tk.Tk()
calculadora = Calculadora(root)
root.mainloop()