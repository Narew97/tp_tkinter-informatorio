
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import time
from datetime import datetime, timedelta
from tkinter import Canvas, Scrollbar, Frame, BOTH, LEFT, RIGHT, Y, VERTICAL


ventana_principal = tk.Tk()
ventana_principal.title("Menú Principal")
ventana_principal.geometry("500x600")
ventana_principal.configure(bg="#7EEA89")

imagen=Image.open("cerveza.jpg")
Imagen=imagen.resize((500,600))
label_tk= ImageTk.PhotoImage(Imagen)

label = tk.Label(ventana_principal,image=label_tk)
label.place(x=0, y=0,relwidth=1,relheight=1)

def actualizar_reloj_y_fecha(): 
        hora_actual = time.strftime("%H:%M:%S")
        fecha_actual = datetime.now().strftime("%d/%m/%Y")
        reloj_label.config(text=hora_actual)
        fecha_label.config(text=fecha_actual)
        ventana_principal.after(1000, actualizar_reloj_y_fecha)

reloj_label = tk.Label(ventana_principal, font=("Arial", 18, "bold"), bg="#7EEA89", fg="black")
reloj_label.place(x=370, y=40)

fecha_label = tk.Label(ventana_principal, font=("Arial", 12), bg="#7EEA89", fg="black")
fecha_label.place(x=370, y=10)

actualizar_reloj_y_fecha()


        
menu_princ = tk.Label( ventana_principal, text="SELECCIONÁ UNA CATEGORÍA DE NUESTRO", font=("Arial", 14, "bold"), bg="#7EEA89", fg="#1b1b1b"
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
        productos_vacuno = [("Costilla", 5500), ("Entraña", 6000),]  
        
        imagenes_vacuno = {
                "Costilla": "costilla_vacun.jpg",
                "Entraña": "entrañ.jpg",
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
        productos_pollo = [("Pollo a la mostaza", 4500), ("Pollo al verdeo", 7800), ("Pollo a la Parrilla", 7000),]  
        
        imagenes_pollo = {
                "Pollo a la mostaza": "pollo_a_la_mostaza.jpg",
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

        imagen = Image.open("hamburguesa con chedar.jpg")
        imagen = imagen.resize((600, 800))
        label_tk = ImageTk.PhotoImage(imagen)
        label = tk.Label(ventana, image=label_tk)
        label.image = label_tk
        label.place(x=0, y=0, relwidth=1, relheight=1)

        tk.Label(ventana, text="Hamburguesas", font=("Helvetica", 18, "bold"), bg="#fcd17e").pack(fill="x", pady=10)

        tk.Label(ventana, text="simple", font=("Helvetica", 16, "bold"), bg="#cf81a8").pack(fill="x", pady=10)
        productos_simple = [("una carne, (jamon, queso,huevo)", 2500), ("doble carne", 4800), ("triple", 8000)]

        for nombre, precio in productos_simple:
                frame = tk.Frame(ventana, bg="#fce4b2")
                frame.pack(anchor="w", padx=20, pady=5, fill="x")
                tk.Label(frame, text=f"{nombre} - ${precio}", font=("Arial", 11), bg="#fce4b2").pack(side="left")
                tk.Button(frame, text="Agregar", command=lambda n=nombre, p=precio: agregar_al_pedido(n, p)).pack(side="right")

        tk.Label(ventana, text="completa", font=("Helvetica", 16, "bold"), bg="#cf81a8").pack(fill="x", pady=15)
        productos_doble = [("una carne,(Queso,jamon,huevo,tomate,lechuga)", 5500), ("doble carne", 6800), ("triple carne", 10000)]

        for nombre, precio in productos_doble:
                frame = tk.Frame(ventana, bg="#fce4b2")
                frame.pack(anchor="w", padx=20, pady=5, fill="x")
                tk.Label(frame, text=f"{nombre} - ${precio}", font=("Arial", 11), bg="#fce4b2").pack(side="left")
                tk.Button(frame, text="Agregar", command=lambda n=nombre, p=precio: agregar_al_pedido(n, p)).pack(side="right")

        tk.Label(ventana, text="con cheddar", font=("Helvetica", 16, "bold"), bg="#cf81a8").pack(fill="x", pady=10)
        productos_cheddar = [("una carne,(Queso,jamon,huevo,tomate,lechuga,panceta)", 4500), ("doble carne", 7800), ("triple carne", 12000)]

        for nombre, precio in productos_cheddar:
                frame = tk.Frame(ventana, bg="#fce4b2")
                frame.pack(anchor="w", padx=20, pady=5, fill="x")
                tk.Label(frame, text=f"{nombre} - ${precio}", font=("Arial", 10), bg="#fce4b2").pack(side="left")
                tk.Button(frame, text="Agregar", command=lambda n=nombre, p=precio: agregar_al_pedido(n, p)).pack(side="right")

        tk.Button(ventana_principal, text="HAMBURGUESAS", width=20, height=2, command=mostrar_hamburguesas).place(x=300, y=60)

def mostrar_pastas():
        ventana = tk.Toplevel()
        ventana.title("Pastas")
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
def mostrar_combos():
        combos = [
                ("Combo 1: Hamburguesa + Papas + Bebida", 7000, "combo1.jpg"),
                ("Combo 2: Pizza + Bebida", 8500, "combo2.jpg"),
                ("Combo 3: Sandwich + Papas + Gaseosa", 7200, "combo3.jpg"),
                ("Combo 4: Hamburguesa doble + Papas", 9500, "combo4.jpg"),
                ("Combo 5: Pizza familiar + 2 Bebidas", 12000, "combo5.jpg"),
]
        mostrar_ventana("Combos", combos)


def mostrar_ventana(titulo, productos):
        ventana = tk.Toplevel()
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

        tk.Label(frame_scroll, text=f"🍽️ {titulo}", font=("Helvetica", 18, "bold"), bg="#ffe8d6").pack(fill="x", pady=10)

        for nombre, precio, imagen_path in productos:
                frame = Frame(frame_scroll, bg="#ffe8d6", bd=1, relief="ridge")
                frame.pack(pady=10, padx=20, fill="x")

                try:
                        img = Image.open(imagen_path)
                        img = img.resize((280, 200))
                        foto = ImageTk.PhotoImage(img)

                        img_label = tk.Label(frame, image=foto)
                        img_label.image = foto
                        img_label.pack()
                except:
                        tk.Label(frame, text="[Imagen no disponible]", bg="#ffe8d6").pack()

                tk.Label(frame, text=f"{nombre} - ${precio}", font=("Arial", 12), bg="#ffe8d6").pack(pady=5)
                tk.Button(frame, text="Agregar al pedido", bg="#ffb703", activebackground="#f48c06",
                                font=("Comic Sans MS", 10), command=lambda n=nombre, p=precio: agregar_al_pedido(n, p)).pack(pady=5)

        tk.Button(frame_scroll, text="🧾 Ver Resumen", font=("Comic Sans MS", 12, "bold"),
                bg="#8ecae6", activebackground="#219ebc", command=ver_resumen).pack(pady=20)

tk.Button(ventana_principal, 
        text="COMBOS", 
        width=20, 
        height=2,
        command=mostrar_combos
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


        try:
                imagen_fondo = Image.open("empanada.jpg")
                imagen_fondo = imagen_fondo.resize((500, 600))
                imagen_tk = ImageTk.PhotoImage(imagen_fondo)
                ventana.imagen_fondo = imagen_tk  

                fondo_label = tk.Label(ventana, image=imagen_tk)
                fondo_label.place(x=0, y=0, relwidth=1, relheight=1)
                fondo_label.lower()
        except Exception as e:
                ventana.configure(bg="#FA8072")


        titulo_frame = tk.Frame(ventana, bg="#FFA500", bd=0, highlightthickness=0)
        titulo_frame.place(x=150, y=20, width=200, height=50)
        tk.Label(
                titulo_frame,
                text="EMPANADAS",
                font=("Helvetica", 18, "bold"),
                bg="#FFA500",
                fg="black"
        ).pack(expand=True, fill="both")

        productos_empanadas = [
                ("Jamón y Queso", 8000),
                ("Pollo", 7500),
                ("Carne picada", 7000),
                ("Carne cortada a cuchillo", 7500),
                ("Verduras", 6500),
                ("Humitas", 7500)
        ]


        y_pos = 90
        for nombre, precio in productos_empanadas:
                producto_frame = tk.Frame(ventana, bg="white", bd=1, relief="solid")
                producto_frame.place(x=50, y=y_pos, width=400, height=35)
                
                tk.Label(producto_frame, text=f"{nombre} - ${precio} c/d", 
                        font=("Arial", 12), bg="white", fg="black").pack(side="left", padx=10, pady=5)
                tk.Button(producto_frame, text="Agregar", bg="#FFA500", fg="black", 
                        font=("Arial", 10, "bold"), 
                        command=lambda n=nombre, p=precio: agregar_al_pedido(n, p)).pack(side="right", padx=10, pady=2)
                
                y_pos += 45

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
        ventana.configure(bg="#ebd28e")
        def actualizar_reloj():
                hora_arg = datetime.utcnow() - timedelta(hours=3)
                ventana.title("Bebidas "+hora_arg.strftime("Hora: %H:%M:%S"))
                ventana.after(1000, actualizar_reloj)

        actualizar_reloj()
        

        imagen=Image.open("mejores-cervezas.jpg")
        imagen=imagen.resize((500,600))
        label_tk= ImageTk.PhotoImage(imagen)

        label = tk.Label(ventana, image=label_tk)
        label.imge= label_tk
        label.place(x=0, y=0,relwidth=1,relheight=1)
        

        tk.Label(ventana, text="BEBIDAS",
                font=("Helvetica", 18, "bold"),
                bg="#ebd28e",
                fg="black"
                ).pack(fill="x", pady=10)


        
        tk.Label(ventana, text="Cervezas", 
                font=("Helvetica", 16, "bold"), 
                bg= "#e9dab3").pack(fill="x", pady=10)
        producto_bebidas = [("Cerveza Hieneken", 5000),
                                ("Cerveza Miller", 3000),
                                ("Cerveza Corona", 6000),]  
        
        for nombre, precio in producto_bebidas:
                frame = tk.Frame(ventana, bg="#c2baa6")
                frame.pack(anchor="w", padx=20, pady=5, fill="x")

                tk.Label(frame, text=f"{nombre} - ${precio}", 
                        font=("Arial", 12), 
                        bg="#c2baa6").pack(side="left")
                tk.Button(frame, text="Agregar", 
                        command=lambda n=nombre, 
                        p=precio: agregar_al_pedido(n, p)
                        ).pack(side="right")

        
        tk.Label(ventana, text="BEBIDAS SIN ALCOHOL", font=("Helvetica", 16, "bold"), 
                bg="#e9dab3").pack(fill="x", 
                                pady=15)
        productos_bebidas = [("Agua", 1500), 
                                ("Coca", 2000)]

        for nombre, precio in productos_bebidas:
                frame = tk.Frame(ventana, bg="#c2baa6")
                frame.pack(anchor="w", padx=20, pady=5, fill="x")

                tk.Label(frame, text=f"{nombre} - ${precio}", 
                        font=("Arial", 12), 
                        bg="#c2baa6").pack(side="left")
                
                tk.Button(frame, text="Agregar", 
                        command=lambda n=nombre, 
                        p=precio: agregar_al_pedido(n, p)
                        ).pack(side="right")
                
        tk.Label(ventana, text="TRAGOS", 
                font=("Helvetica", 16, "bold"), 
                bg="#e9dab3").pack(fill="x", pady=10)
        productos_bebidas = [("Daikiri", 3000), 
                                ("Vodka", 7800),
                                ("Lemongin", 3000),]  
        
        for nombre, precio in productos_bebidas:
                frame = tk.Frame(ventana, bg="#c2baa6")
                frame.pack(anchor="w", padx=20, pady=5, fill="x")

                tk.Label(frame, text=f"{nombre} - ${precio}", 
                        font=("Arial", 12), bg="#c2baa6").pack(side="left")
                tk.Button(frame, text="Agregar", 
                        command=lambda n=nombre, 
                        p=precio: agregar_al_pedido(n, p)
                        ).pack(side="right")


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
        
        tk.Label(ventana, text="POSTRES", 
                font=("Helvetica", 18, "bold"), 
                bg="#fcd17e"
                ).pack(fill="x", pady=10)


        lista_postres = [
                ("Lemon Pie", 10000),
                ("Vigilante", 8000),
                ("Flan", 2500),
                ("Torta Chaja", 12000),
                ("Alfajores de Maicena", 8000)
        ]
        imagenes_postres = {
                "Lemon Pie":"lemonpie.jpg",
                "Vigilante":"vigilante.jpg",
                "Flan":"flan.jpeg",
                "Torta Chaja":"tortachaja.jpeg",
                "Alfajores de Maicena":"Alfajores de Maicena.jpeg"
        }
        for nombre, precio in lista_postres:     
                frame = tk.Frame(ventana, bg="#d1ecf3")
                frame.pack(anchor="w", padx=0, pady=0, fill="x")
                
                rut_img= imagenes_postres.get(nombre,)
                img = Image.open(rut_img)
                img = img.resize((60, 60))
                foto = ImageTk.PhotoImage(img)
                
                img_label = tk.Label(frame, image=foto, bg="#fce4b2")
                img_label.image = foto 
                img_label.pack(side="left", padx=0, pady=0)

                tk.Label(frame, text=f"{nombre} - ${precio}", font=("Arial", 12), bg="#d1ecf3").pack(side="left")
                tk.Button(frame, text="Agregar", 
                        command=lambda n=nombre, p=precio: agregar_al_pedido(n, p)
                        ).pack(side="right")

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
        resumen.configure(bg="#faf3e0")



        total = 0
        tk.Label(resumen, text="Detalles del Pedido", 
                font=("Arial", 16, "bold"),

                ).pack(pady=10)

        for producto, precio in pedido:
                tk.Label(resumen, text=f"{producto} - ${precio}", font=("Arial", 12, ),bg="#faf3e0").pack(anchor="w", padx=20)
                total += precio

        tk.Label(resumen, text=f"\nTOTAL: ${total}", font=("Arial", 14, "bold"),bg="#faf3e0").pack(pady=20)
        

tk.Button(ventana_principal, 
        text="Ver Pedido", 
        bg="#fcd17e", 
        font=("Arial", 12, "bold"), 
        command=ver_resumen).place(x=200, y=500)
#################################################

ventana_principal.mainloop()
