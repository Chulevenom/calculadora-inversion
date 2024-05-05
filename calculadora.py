import tkinter as tk
from tkinter import messagebox
from tkinter import Label, StringVar, Entry

def calcular_rendimiento(importe, tna):
    importe = int(importe)
    tna = int(tna)
    
    tna_x_mes = tna / 12
    tna_e_importe = (importe * tna_x_mes) / 100
    suma_total = tna_e_importe / 30
    messagebox.showinfo("Resultado", "Rendimiento mensual Total: $" + str(tna_e_importe) + "\nRendimiento por día: $" + str(suma_total))


root = tk.Tk()
root.geometry('350x100')
root.title('Calculadora de Rendimiento')
label= Label(root, text="Ingrese Monto y TNA") 
label.pack()
importe = StringVar()
tna = StringVar()
Ent1 = Entry(root, textvariable=importe)
Ent1.pack()
Ent2 = Entry(root, textvariable=tna)
Ent2.pack()
boton_leer = tk.Button(root,text="Calcular", command=lambda: calcular_rendimiento(importe.get(), tna.get()),bg='lightgreen',font =('calibri', 12)) 
boton_leer.pack()
root.mainloop()