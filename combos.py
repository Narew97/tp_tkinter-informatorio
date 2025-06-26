from tkinter import *
from PIL import Image, ImageTk

pedido = []

font_titulo = ("Comic Sans MS", 18, "bold")
font_texto = ("Comic Sans MS", 12)

# -------- AGREGAR PRODUCTO AL PEDIDO --------
def agregar_al_pedido(nombre, precio):
    pedido.append((nombre, precio))

# -------- VER RESUMEN --------
def ver_resumen():
    resumen = Toplevel()
    resumen.title("Resumen de Pedido")
    resumen.geometry("400x400")
    resumen.configure(bg="#faf3e0")

    Label(resumen, text="🧾 Tu Pedido", font=font_titulo, bg="#faf3e0").pack(pady=10)

    total = 0
    for producto, precio in pedido:
        Label(resumen, text=f"{producto} - ${precio}", font=font_texto, bg="#faf3e0").pack(anchor="w", padx=10)
        total += precio

    Label(resumen, text=f"\nTotal: ${total}", font=font_titulo, bg="#faf3e0").pack(pady=10)

# -------- VENTANA CON PRODUCTOS --------
def mostrar_ventana(titulo, productos):
    ventana = Toplevel()
    ventana.title(titulo)
    ventana.geometry("530x700")
    ventana.configure(bg="#faf3e0")

    canvas = Canvas(ventana, bg="#615639", highlightthickness=0)
    scrollbar = Scrollbar(ventana, orient=VERTICAL, command=canvas.yview)
    frame_scroll = Frame(canvas, bg="#ad903e")

    frame_scroll.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=frame_scroll, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.pack(side=RIGHT, fill=Y)

    Label(frame_scroll, text=f"🍽️ {titulo}", font=font_titulo, bg="#ffe8d6").pack(fill="x", pady=10)

    for nombre, precio, imagen_path in productos:
        frame = Frame(frame_scroll, bg="#ffe8d6", bd=1, relief="ridge")
        frame.pack(pady=10, padx=20, fill="x")

        try:
            img = Image.open(imagen_path)
            img = img.resize((280, 200))
            foto = ImageTk.PhotoImage(img)

            img_label = Label(frame, image=foto)
            img_label.image = foto
            img_label.pack()
        except:
            Label(frame, text="[Imagen no disponible]", bg="#ffe8d6").pack()

        Label(frame, text=f"{nombre} - ${precio}", font=font_texto, bg="#ffe8d6").pack(pady=5)
        Button(frame, text="Agregar al pedido", bg="#ffb703", activebackground="#f48c06",
               font=("Comic Sans MS", 10), command=lambda n=nombre, p=precio: agregar_al_pedido(n, p)).pack(pady=5)

    Button(frame_scroll, text="🧾 Ver Resumen", font=("Comic Sans MS", 12, "bold"),
           bg="#8ecae6", activebackground="#219ebc", command=ver_resumen).pack(pady=20)

# -------- FUNCIONES PARA CADA TIPO --------
def mostrar_combos():
    combos = [
        ("Combo 1: Hamburguesa + Papas + Bebida", 7000, "combo1.jpg"),
        ("Combo 2: Pizza + Bebida", 8500, "combo2.jpg"),
        ("Combo 3: Sandwich + Papas + Gaseosa", 7200, "combo3.jpg"),
        ("Combo 4: Hamburguesa doble + Papas", 9500, "combo4.jpg"),
        ("Combo 5: Pizza familiar + 2 Bebidas", 12000, "combo5.jpg"),
    ]
    mostrar_ventana("Combos", combos)

def mostrar_postres():
    postres = [
        ("Lemon Pie", 10000, "lemon.jpg"),
        ("Flan", 2500, "flan.jpg"),
        ("Torta Chajá", 12000, "chaja.jpg"),
        ("Alfajores de Maicena", 8000, "alfajor.jpg"),
        ("Vigilante", 8000, "vigilante.jpg"),
    ]
    mostrar_ventana("Postres", postres)

def mostrar_bebidas():
    bebidas = [
        ("Cerveza Heineken", 5000, "heineken.jpg"),
        ("Cerveza Miller", 3000, "miller.jpg"),
        ("Cerveza Corona", 6000, "corona.jpg"),
        ("Coca-Cola", 2000, "coca.jpg"),
        ("Agua", 1500, "agua.jpg"),
        ("Daikiri", 3000, "daikiri.jpg"),
        ("Vodka", 7800, "vodka.jpg"),
        ("Lemongin", 3000, "lemongin.jpg"),
    ]
    mostrar_ventana("Bebidas", bebidas)

# -------- VENTANA PRINCIPAL --------
root = Tk()
root.title("Menú Principal")
root.geometry("400x400")
root.configure(bg="#faf3e0")

Label(root, text="Menú", font=("Comic Sans MS", 20, "bold"), bg="#faf3e0").pack(pady=20)

Button(root, text="🍔 Combos", font=font_texto, bg="#ffb703", width=20, command=mostrar_combos).pack(pady=10)
Button(root, text="🍰 Postres", font=font_texto, bg="#ffb703", width=20, command=mostrar_postres).pack(pady=10)
Button(root, text="🥤 Bebidas", font=font_texto, bg="#ffb703", width=20, command=mostrar_bebidas).pack(pady=10)

root.mainloop()
