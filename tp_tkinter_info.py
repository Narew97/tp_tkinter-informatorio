
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

ventana_principal = tk.Tk()
ventana_principal.title("Menú Principal")
ventana_principal.geometry("500x600")
ventana_principal.configure(bg="#7EEA89")

menu_princ=tk.Label(ventana_principal, 
        text="Seleccioná una categoría de nuestro menú", 
        font=("Arial", 14),bg="#7EEA89"
        )
menu_princ.pack(pady=10)

########################FUNCION PARA AGREGAR PRODUCTOS AL PEDIDO###################################3
pedido = []  

def agregar_al_pedido(producto, precio):
    pedido.append((producto, precio))
    messagebox.showinfo("Agregado", f"{producto} agregado al pedido.")


######################### FUNCION DE SECCION CARNES #############################################
def mostrar_carnes():
    ventana = tk.Toplevel()
    ventana.title("CARNES")
    ventana.geometry("500x800")
    ventana.configure(bg="#fce4b2")
    

    imagen = Image.open("fondomcarnes.jpg")
    imagen = imagen.resize((800, 1200))
    label_tk = ImageTk.PhotoImage(imagen)
    label = tk.Label(ventana, image=label_tk)
    label.image = label_tk
    label.place(x=0, y=0, relwidth=1, relheight=1)
    
    tk.Label(ventana, text="CARNES", 
            font=("Helvetica", 18, "bold"), 
            bg="#fcd17e"
            ).pack(fill="x", pady=1)
    
    tk.Label(ventana, text="VACUNO", font=("Helvetica", 16, "bold"), bg="#cf81a8").pack(fill="x", pady=10)
    productos_vacuno = [("costilla", 5500), ("entraña", 6000),]  
    
    imagenes_vacuno = {
        "costilla": "costilla_vacun.jpg",
        "lomo": "lomodevaca.jpg",
        "entraña": "entrañ.jpg",
    }
    for nombre, precio in productos_vacuno:
        frame = tk.Frame(ventana, bg="#fff9ed")
        frame.pack(anchor="w", padx=0, pady=0, fill="x")

        rut_img= imagenes_vacuno.get(nombre,)
        img = Image.open(rut_img)
        img = img.resize((60, 60))
        foto = ImageTk.PhotoImage(img)
    
        img_label = tk.Label(frame, image=foto, bg="#fce4b2")
        img_label.image = foto 
        img_label.pack(side="left", padx=0, pady=0)
        
        

        tk.Label(frame, text=f"{nombre} - ${precio}", font=("Arial", 12), bg="#fff9ed").pack(side="left")
        tk.Button(frame, text="Agregar", 
                command=lambda n=nombre, 
                p=precio: agregar_al_pedido(n, p)
                ).pack(side="right")

    
    tk.Label(ventana, text="CERDO", font=("Helvetica", 16, "bold"), bg="#f3c6dc").pack(fill="x", pady=10)
    productos_cerdo = [("Costilla", 4500), ("Lomo de cerdo agridulce", 6800),("Arrollado de cerdo", 10000) ]

    imagenes_cerdo = {
        "Costilla": "costilladecerdo.jpg",
        "Lomo de cerdo agridulce": "cerdagrid.jpg",
        "Arrollado de cerdo": "lomo_de_cerdo.jpg",
}

    for nombre, precio in productos_cerdo:
        frame = tk.Frame(ventana, bg="#fff9ed")
        frame.pack(anchor="w", padx=0, pady=0, fill="x")

        rut_img= imagenes_cerdo.get(nombre,)
        img = Image.open(rut_img)
        img = img.resize((60, 60))
        foto = ImageTk.PhotoImage(img)
    
        img_label = tk.Label(frame, image=foto, bg="#fce4b2")
        img_label.image = foto 
        img_label.pack(side="left", padx=0, pady=0)
        
        
    
        tk.Label(frame, text=f"{nombre} - ${precio}", font=("Arial", 11), bg="#fff9ed").pack(side="left", padx=10)
        
        tk.Button(frame, text="Agregar", 
                command=lambda n=nombre, 
                p=precio: agregar_al_pedido(n, p)
                ).pack(side="right")
        
    tk.Label(ventana, text="POLLO", font=("Helvetica", 16, "bold"), bg="#d5bbc8").pack(fill="x", pady=10)
    productos_pollo = [("Pollo a la moztaza", 4500), ("Pollo al verdeo", 7800), ("Pollo a la Parrilla", 7000),]  
    
    imagenes_pollo = {
        "Pollo a la moztaza": "pollo_a_la_mostaza.jpg",
        "Pollo al verdeo": "pollo_al_verdeo.jpg",
        "Pollo a la Parrilla": "pollo_a_la_parrilla.jpg",
    }
    
    for nombre, precio in productos_pollo:
        frame = tk.Frame(ventana, bg="#fff9ed")
        frame.pack(anchor="w", padx=0, pady=0, fill="x")
        
        rut_img= imagenes_pollo.get(nombre,)
        img = Image.open(rut_img)
        img = img.resize((60, 60))
        foto = ImageTk.PhotoImage(img)
    
        img_label = tk.Label(frame, image=foto, bg="#fce4b2")
        img_label.image = foto 
        img_label.pack(side="left", padx=0, pady=0)

        tk.Label(frame, text=f"{nombre} - ${precio}", font=("Arial", 12), bg="#fff9ed").pack(side="left")
        tk.Button(frame, text="Agregar", 
                command=lambda n=nombre, 
                p=precio: agregar_al_pedido(n, p)
                ).pack(side="right")

        

tk.Button(ventana_principal, 
        text="CARNES", 
        width=20, 
        height=2,
        command=mostrar_carnes
        ).place(x=50, y=60)


################# FUNCION DE SECCION HAMBURGUESAS #################
def mostrar_hamburguesas():
    ventana = tk.Toplevel()
    ventana.title("Hamburguesas")
    ventana.geometry("500x600")
    ventana.configure(bg="#d1ecf3")


tk.Button(ventana_principal, 
        text="HAMBURGUESAS", 
        width=20, 
        height=2,
        command=mostrar_hamburguesas
        ).place(x=300, y=60)


######################## FUNCION DE SECCION PASTAS ########################
def mostrar_pastas():
    ventana = tk.Toplevel()
    ventana.title("Pastas")
    ventana.geometry("500x600")
    ventana.configure(bg="#d1ecf3")

tk.Button(ventana_principal, 
        text="PASTAS", 
        width=20, 
        height=2,
        command=mostrar_pastas
        ).place(x=50, y=180)

######################## FUNCION DE SECCION SANDWICHES ########################
def mostrar_sandwiches():
    ventana = tk.Toplevel()
    ventana.title("Sandwiches")
    ventana.geometry("500x600")
    ventana.configure(bg="#d1ecf3")

tk.Button(ventana_principal, 
        text="SANDWICHES", 
        width=20, 
        height=2,
        command=mostrar_sandwiches
        ).place(x=300, y=180)

########################FUNCION DE SECCION PIZZAS ########################
def mostrar_pizzas():
    ventana = tk.Toplevel()
    ventana.title("Pizzas")
    ventana.geometry("500x600")
    ventana.configure(bg="#d4c39b")


tk.Button(ventana_principal, 
        text="PIZZAS", 
        width=20, 
        height=2,
        command=mostrar_pizzas
        ).place(x=300, y=300)

######################## FUNCION DE SECCION EMPANADAS ########################
def mostrar_empanadas():
    ventana = tk.Toplevel()
    ventana.title("Empanadas")
    ventana.geometry("500x600")
    ventana.configure(bg="#FA8072")  

    tk.Label(
        ventana,
        text="EMPANADAS",
        font=("Helvetica", 18, "bold"),
        bg="",  
        fg="black"
    ).pack(fill="x", pady=10)

    productos_empanadas = [
        ("Jamon y Queso", 8000),
        ("Pollo", 7500),
        ("Carne picada", 7000),
        ("Carne cortada a cuchillo", 7500),
        ("Verduras", 6500),
        ("Humitas", 7500)
    ]

    for nombre, precio in productos_empanadas:
        frame = tk.Frame(ventana, bg="#FA8072")
        frame.pack(anchor="w", padx=20, pady=5, fill="x")

        tk.Label(frame, text=f"{nombre} - ${precio} c/d", font=("Arial", 12), bg="#FA8072").pack(side="left")
        tk.Button(frame, text="Agregar", command=lambda n=nombre, p=precio: agregar_al_pedido(n, p)).pack(side="right")


tk.Button(ventana_principal, 
        text="EMPANADAS", 
        width=20, 
        height=2,
        command=mostrar_empanadas
        ).place(x=50, y=300)

######################## FUNCION DE SECCION BEBIDAS ########################
def mostrar_bebidas():
    ventana = tk.Toplevel()
    ventana.title("Bebidas")
    ventana.geometry("500x600")
    ventana.configure(bg="#d1ecf3")

tk.Button(ventana_principal, 
        text="BEBIDAS", 
        width=20, 
        height=2,
        command=mostrar_bebidas
        ).place(x=50, y=420)

######################## FUNCION DE SECCION POSTRES ########################
def mostrar_postres():
    ventana = tk.Toplevel()
    ventana.title("Postres")
    ventana.geometry("500x600")
    ventana.configure(bg="#d1ecf3")

tk.Button(ventana_principal, 
        text="POSTRES", 
        width=20, 
        height=2,
        command=mostrar_postres
        ).place(x=300, y=420)

#################################### FUNCION PARA VER EL RESUMEN DEL PEDIDO ####################################
def ver_resumen():
    if not pedido:
        messagebox.showinfo("Detalles del Pedido", "No hay productos aún.")
        return

    resumen = tk.Toplevel()
    resumen.title("DETALLES DEL PEDIDO")
    resumen.geometry("500x600")
    resumen.configure(bg="#cfeace")

    total = 0
    tk.Label(resumen, text="Detalles del Pedido", 
            font=("Arial", 16, "bold"),

            ).pack(pady=10)

    for producto, precio in pedido:
        tk.Label(resumen, text=f"{producto} - ${precio}", font=("Arial", 12)).pack(anchor="w", padx=20)
        total += precio

    tk.Label(resumen, text=f"\nTOTAL: ${total}", font=("Arial", 14, "bold")).pack(pady=20)
    

tk.Button(ventana_principal, 
        text="Ver Pedido", 
        bg="#fcd17e", 
        font=("Arial", 12, "bold"), 
        command=ver_resumen).place(x=200, y=500)
#################################################

ventana_principal.mainloop()