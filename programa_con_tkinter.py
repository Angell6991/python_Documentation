import tkinter as tk

ventana     =   tk.Tk()
ventana.geometry("400x300")


etiqueta    =   tk.Label(ventana, text= "Hola mundo", bg="blue" )
etiqueta.pack(side= tk.BOTTOM, fill= tk.Y, expand=True)

def saludo():
    return print("Hola")

boton1  = tk.Button(ventana,text="boton",command= saludo)
boton1.pack()

cajaTexto   =   tk.Entry(ventana,font= "Inconsolata 15")
cajaTexto.pack()

def texto_de_la_caja():
    texx = cajaTexto.get()
    return print(texx)

boton2  = tk.Button(ventana,text="texto2",command= texto_de_la_caja)
boton2.pack()

"""
boton11  = tk.Button(ventana,text="texto11")
boton22  = tk.Button(ventana,text="texto22")
boton33  = tk.Button(ventana,text="texto33")

boton11.grid(row=0, column=0)
boton22.grid(row=1, column=1)
boton33.grid(row=2, column=2)
"""
ventana.mainloop()

