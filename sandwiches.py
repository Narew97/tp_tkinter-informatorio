def mostrar_sandwiches():
    ventana = tk.Toplevel()
    ventana.title("Menú sandwiches")
    ventana.geometry("500x600")
    ventana.configure(bg="#d1ecf3")
    
    tk.Label(ventana, text="Sandwiches", 
            font=("Helvetica", 18, "bold"), 
            bg="#fcd17e"
            ).pack(fill="x", pady=10)
    
    tk.Label(ventana, text="Sandwiches", font=("Helvetica", 16, "bold"), bg="#cf81a8").pack(fill="x", pady=10)
    producto_sandwiches = [("Sandwiches", 5500), ("lomo", 7800), ("entraña", 6000),]  
    
    for nombre, precio in producto_postre:
        frame = tk.Frame(ventana, bg="#fce4b2")
        frame.pack(anchor="w", padx=20, pady=5, fill="x")

        tk.Label(frame, text=f"{nombre} - ${precio}", font=("Arial", 12), bg="#fce4b2").pack(side="left")
        tk.Button(frame, text="Agregar", 
                command=lambda n=nombre, 
                p=precio: agregar_al_pedido(n, p)
                ).pack(side="right")

    
    tk.Label(ventana, text="CERDO", font=("Helvetica", 16, "bold"), bg="#cf81a8").pack(fill="x", pady=15)
    productos_cerdo = [("costilla", 4500), ("lomo", 6800)]

    for nombre, precio in productos_cerdo:
        frame = tk.Frame(ventana, bg="#fce4b2")
        frame.pack(anchor="w", padx=20, pady=5, fill="x")

        tk.Label(frame, text=f"{nombre} - ${precio}", font=("Arial", 12), bg="#fce4b2").pack(side="left")
        
        tk.Button(frame, text="Agregar", 
                command=lambda n=nombre, 
                p=precio: agregar_al_pedido(n, p)
                ).pack(side="right")
        
    tk.Label(ventana, text="Postre", font=("Helvetica", 16, "bold"), bg="#cf81a8").pack(fill="x", pady=10)
    productos_pollo = [("Pollo a la moztaza", 4500), ("Pollo al verdeo", 7800), ("Pollo a la Parrilla", 7000),]  
    
    for nombre, precio in productos_pollo:
        frame = tk.Frame(ventana, bg="#fce4b2")
        frame.pack(anchor="w", padx=20, pady=5, fill="x")

        tk.Label(frame, text=f"{nombre} - ${precio}", font=("Arial", 12), bg="#fce4b2").pack(side="left")
        tk.Button(frame, text="Agregar", 
                command=lambda n=nombre, 
                p=precio: agregar_al_pedido(n, p)
                ).pack(side="right")

tk.Button(ventana_principal, 
        text="POSTRES", 
        width=20, 
        height=2,
        command=mostrar_postres
        ).place(x=300, y=420)