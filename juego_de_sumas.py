from tkinter import *
from random import randint

#-----raiz------------------
root = Tk()
root.title("Juego de Sumas")
root.geometry("300x400")
root.config(bg="pink")
root.resizable(0,0)

#-----variables-------------
a = 0
b = 0
total = None
#-----funciones-------------

def mostar_sumas(a, b): 
    a = randint(0, 10)
    b = randint(0, 10)
    global total
    total = a + b
    label = Label(root, text=f"Cuanto es {a}+{b}?", bg="pink", fg="purple", font=("arial", 20))
    label.grid(row=0, column=0, columnspan=4)

def igual():
    total_usuario = entrada.get()
    if str(total) == total_usuario:
        label1.config(text="Tu resultado está bien")
        entrada.delete(0, END)
        mostar_sumas(a, b)
    else:
        label1.config(text="Sigue intentándolo")
 
def envia_boton(valor):
	anterior = entrada.get()
	entrada.delete(0, END)
	entrada.insert(0, str(anterior) + str(valor))
        
def borrar():
	entrada.delete(0, END)
        
               
#-----etiqueta de sumas-----

label = Label(root, COMMAND=mostar_sumas(a, b))

#-----entry-----------------

entrada = Entry(root)
entrada.config(fg="purple", font=("arial", 20))
entrada.grid(row=1, column=0, columnspan=4)


#-----botones 1ra fila ---------------

boton1 = Button(root, text="1", 
                bg="pink" ,
                fg="purple",command=lambda: envia_boton(1), 
                padx=25, pady=15).grid(row=3, column=0)

boton2 = Button(root, text="2", 
                bg="pink" ,
                fg="purple",command=lambda: envia_boton(2),  
                padx=25, pady=15).grid(row=3, column=1)

boton3 = Button(root, text="3", 
                bg="pink" ,
                fg="purple", command=lambda: envia_boton(3), 
                padx=25, pady=15).grid(row=3, column=2)

#-----botones 2da fila ---------------

boton4 = Button(root, text="4", 
                bg="pink" ,
                fg="purple",command=lambda: envia_boton(4),  
                padx=25, pady=15).grid(row=4, column=0)

boton5 = Button(root, text="5", 
                bg="pink" ,
                fg="purple", command=lambda: envia_boton(5), 
                padx=25, pady=15).grid(row=4, column=1)

boton6 = Button(root, text="6", 
                bg="pink" ,
                fg="purple", command=lambda: envia_boton(6), 
                padx=25, pady=15).grid(row=4, column=2)

#-----botones 3ra fila ---------------

boton7 = Button(root, text="7", 
                bg="pink" ,
                fg="purple", command=lambda: envia_boton(7), 
                padx=25, pady=15).grid(row=5, column=0)

boton8 = Button(root, text="8", 
                bg="pink" ,
                fg="purple", command=lambda: envia_boton(8), 
                padx=25, pady=15).grid(row=5, column=1)

boton9 = Button(root, text="9", 
                bg="pink" ,
                fg="purple", command=lambda: envia_boton(9), 
                padx=25, pady=15).grid(row=5, column=2)

#-----botones 4ta fila ---------------

boton_borrar = Button(root, text="C.", 
                bg="pink" ,
                fg="purple", command=lambda: borrar(),
                padx=25, pady=15).grid(row=6, column=0)

boton0 = Button(root, text="0", 
                bg="pink" ,
                fg="purple", command=lambda: envia_boton(0), 
                padx=25, pady=15).grid(row=6, column=1)

boton_igual = Button(root, text="=", 
                bg="pink" ,
                fg="purple", command=igual,
                padx=25, pady=15).grid(row=6, column=2)


#-----etiqueta de sumas-----

label1 = Label(root, bg="pink", fg="purple", font=("arial", 20))
label1.grid(row=8, column=0, columnspan=4)





root.mainloop()