import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import datetime

#precio de las pizzas
pizzas = [
    {"nombre": "MUZZARELLA", "precio $": 4500, "imagen": "muzzarella.jpg"},
    {"nombre": "ESPECIAL", "precio $": 5500, "imagen": "especial.jpg"},
    {"nombre": "Cuatro Quesos", "precio $": 6500, "imagen": "cuatro_queso.jpg"}
]

def calcular_precios(precio_base, iva):
    precio_final = precio_base * (1 + iva / 100)
    return {
        "lista": round(precio_final, 2),
        "tarjeta": round(precio_final * 1.05, 2),
        "transferencia": round(precio_final * 0.95, 2),
        "qr": round(precio_final * 0.90, 2)
    }

def cargar_imagen(ruta, tamaño=(120, 120)):
    try:
        img = Image.open(ruta).resize(tamaño)
        return ImageTk.PhotoImage(img)
    except:
        return None

def mostrar_menu_pizzas():
    for widget in frame_scroll.winfo_children():
        widget.destroy()

    try:
        iva = float(entry_iva.get())
    except:
        iva = 0

    for i, pizza in enumerate(pizzas):
        precios = calcular_precios(pizza["precio $"], iva)
        imagen = cargar_imagen(pizza["imagen"])

        frame_pizza = tk.Frame(frame_scroll, bg="#fef9e7", relief="ridge", bd=2)
        frame_pizza.pack(pady=15)

        interno = tk.Frame(frame_pizza, bg="#fef9e7")
        interno.pack(padx=10, pady=10)

        if imagen:
            img_label = tk.Label(interno, image=imagen, bg="#fef9e7")
            img_label.pack(pady=5)
            frame_pizza.image = imagen

        info = (
            f"{pizza['nombre']}\n\n"
            f"Lista: ${precios['lista']}\n"
            f"Tarjeta: ${precios['tarjeta']}\n"
            f"Transferencia: ${precios['transferencia']}\n"
            f"QR: ${precios['qr']}"
        )

        text_label = tk.Label(
            interno,
            text=info,
            font=("Segoe Print", 11),
            justify="center",
            anchor="center",
            bg="#fef9e7"
        )
        text_label.pack(pady=5)

# Ventana principal
root = tk.Tk()
root.title("Menú PIZZAS")
root.geometry("800x700")
root.configure(bg="light salmon")

# Fecha y hora
hora_label = tk.Label(root, text=datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                      font=("Helvetica", 10), bg="#d6eaf8")
hora_label.pack(pady=5)

# IVA
frame_top = tk.Frame(root, bg="#d60fd6")
frame_top.pack()
tk.Label(frame_top, text="IVA (%)", bg="#1cd8c8").pack(side="left")
entry_iva = tk.Entry(frame_top, width=5)
entry_iva.insert(0, "21")
entry_iva.pack(side="left", padx=5)

# Botón menú
btn_menu = tk.Button(root, text="PIZZAS", command=mostrar_menu_pizzas, font=("Impact", 14), bg="cyan")
btn_menu.pack(pady=10)

# se centro la imagen al medio
contenedor_canvas = tk.Frame(root, bg="light salmon")
contenedor_canvas.pack(expand=True, fill="both")

canvas = tk.Canvas(contenedor_canvas, highlightthickness=0, bg="#e9b610")
scrollbar = ttk.Scrollbar(contenedor_canvas, orient="vertical", command=canvas.yview)

frame_scroll = tk.Frame(canvas, bg="#e9b610")

canvas.create_window((0, 0), window=frame_scroll, anchor="n", width=750)
canvas.configure(yscrollcommand=scrollbar.set)

frame_scroll.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

root.mainloop()