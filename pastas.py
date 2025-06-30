import tkinter as tk
from tkinter import messagebox
from turtle import width
from PIL import Image, ImageTk


ventana_principal = tk.Tk()
ventana_principal.title("Menú Principal")
ventana_principal.geometry("500x600")
ventana_principal.configure(bg="#7EEA89")

menu_princ = tk.Label(
    ventana_principal,
    text="Seleccioná una categoría de nuestro menú",
    font=("Arial", 14),
    bg="#7EEA89",
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
    ventana.geometry("500x600")
    ventana.configure(bg="#fce4b2")

tk.Button(
    ventana_principal, text="CARNES", width=20, height=2, command=mostrar_carnes
).place(x=50, y=60)


################# FUNCION DE SECCION HAMBURGUESAS #################
def mostrar_hamburguesas():
    ventana = tk.Toplevel()
    ventana.title("Hamburguesas")
    ventana.geometry("500x600")
    ventana.configure(bg="#d1ecf3")


tk.Button(
    ventana_principal,
    text="HAMBURGUESAS",
    width=20,
    height=2,
    command=mostrar_hamburguesas,
).place(x=300, y=60)


######################## FUNCION DE SECCION PASTAS ########################
def mostrar_pastas():
    ventana = tk.Toplevel()
    ventana.title("Pastas")
    ventana.geometry("500x600")
    ventana.configure(bg="#d1ecf3")

    # Cargar y configurar imagen de fondo
    try:
        imagen_fondo = Image.open("pasta.png")
        imagen_fondo = imagen_fondo.resize(
            (500, 600)
        )  # redimenciona la imagen al contenedor
        imagen_tk = ImageTk.PhotoImage(imagen_fondo)
        ventana.imagen_fondo = imagen_tk  # Mantener referencia

        fondo_label = tk.Label(ventana, image=imagen_tk)
        fondo_label.place(x=0, y=0, relwidth=1, relheight=1)
        fondo_label.lower()
    except Exception as e:
        ventana.configure(bg="#FFFFFF")

    titulo_frame = tk.Frame(ventana, bg="#FFA500", bd=0, highlightthickness=0)
    titulo_frame.place(x=150, y=20, width=200, height=50)
    tk.Label(
        titulo_frame,
        text="PASTAS",
        font=("Tahoma", 30, "bold"),
        fg="black",
    ).pack(expand=True, fill="both")

    pastas = [
        ("Espaguetis", 8500.0),
        ("Tallarines", 8500.0),
        ("Fettuccine", 9500.0),
        ("Vermicelli", 9500.0),
        ("Ringuini", 10000.0),
        ("Ravioles", 7500.0),
        ("Canelones", 7500.0),
        ("Sorrentinos", 7500.0),
        ("Cappelletti", 6500.0),
    ]

    # Contenedor para los productos
    y_pos = 90  # ubicacion inicial
    for nombre, precio in pastas:
        producto_frame = tk.Frame(ventana, bg="white", bd=1, relief="solid")
        producto_frame.place(x=50, y=y_pos, width=400, height=35)

        tk.Label(
            producto_frame,
            text=f"{nombre} \t ${precio} ",
            font=("Consolas", 14),
            bg="white",
            fg="black",
        ).pack(side="left", padx=10, pady=5)
        tk.Button(
            producto_frame,
            text="Agregar",
            bg="#00FFA6",
            fg="black",
            font=("Arial", 10, "bold"),
            command=lambda n=nombre, p=precio: agregar_al_pedido(n, p),
        ).pack(side="right", padx=2)

        y_pos += 50  # ubicacion


tk.Button(
    ventana_principal, text="PASTAS", width=20, height=2, command=mostrar_pastas
).place(x=50, y=180)


######################## FUNCION DE SECCION SANDWICHES ########################
def mostrar_sandwiches():
    ventana = tk.Toplevel()
    ventana.title("Sandwiches")
    ventana.geometry("500x600")
    ventana.configure(bg="#d1ecf3")


tk.Button(
    ventana_principal, text="SANDWICHES", width=20, height=2, command=mostrar_sandwiches
).place(x=300, y=180)


########################FUNCION DE SECCION PIZZAS ########################
def mostrar_pizzas():
    ventana = tk.Toplevel()
    ventana.title("Pizzas")
    ventana.geometry("500x600")
    ventana.configure(bg="#d4c39b")


tk.Button(
    ventana_principal, text="PIZZAS", width=20, height=2, command=mostrar_pizzas
).place(x=300, y=300)


######################## FUNCION DE SECCION EMPANADAS ########################
def mostrar_empanadas():
    ventana = tk.Toplevel()
    ventana.title("Empanadas")
    ventana.geometry("500x600")


tk.Button(
    ventana_principal, text="EMPANADAS", width=20, height=2, command=mostrar_empanadas
).place(x=50, y=300)


######################## FUNCION DE SECCION BEBIDAS ########################
def mostrar_bebidas():
    ventana = tk.Toplevel()
    ventana.title("Bebidas")
    ventana.geometry("500x600")
    ventana.configure(bg="#d1ecf3")


tk.Button(
    ventana_principal, text="BEBIDAS", width=20, height=2, command=mostrar_bebidas
).place(x=50, y=420)


######################## FUNCION DE SECCION POSTRES ########################
def mostrar_postres():
    ventana = tk.Toplevel()
    ventana.title("Postres")
    ventana.geometry("500x600")
    ventana.configure(bg="#d1ecf3")


tk.Button(
    ventana_principal, text="POSTRES", width=20, height=2, command=mostrar_postres
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
    tk.Label(
        resumen,
        text="Detalles del Pedido",
        font=("Arial", 16, "bold"),
    ).pack(pady=10)

    for producto, precio in pedido:
        tk.Label(resumen, text=f"{producto} - ${precio}", font=("Arial", 12)).pack(
            anchor="w", padx=20
        )
        total += precio

    tk.Label(resumen, text=f"\nTOTAL: ${total}", font=("Arial", 14, "bold")).pack(
        pady=20
    )


tk.Button(
    ventana_principal,
    text="Ver Pedido",
    bg="#fcd17e",
    font=("Arial", 12, "bold"),
    command=ver_resumen,
).place(x=200, y=500)
#################################################

ventana_principal.mainloop()
