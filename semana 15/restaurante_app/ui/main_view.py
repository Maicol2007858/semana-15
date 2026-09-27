import tkinter as tk
from tkinter import ttk, messagebox

from servicios.restaurante_servicio import RestauranteServicio


class MainView:

    def __init__(self, root):
        self.root = root
        self.servicio = RestauranteServicio()

        self.root.title("Restaurante App")
        self.root.geometry("900x600")

        self.crear_interfaz()

    def crear_interfaz(self):

        titulo = tk.Label(
            self.root,
            text="RESTAURANTE APP",
            font=("Arial", 22, "bold")
        )
        titulo.pack(pady=15)

        notebook = ttk.Notebook(self.root)
        notebook.pack(fill="both", expand=True, padx=20, pady=10)

        self.tab_ventas = ttk.Frame(notebook)

        notebook.add(self.tab_ventas, text="Ventas")

        self.crear_ventas()

    def crear_ventas(self):

        titulo = tk.Label(
            self.tab_ventas,
            text="Registro de Ventas",
            font=("Arial", 18, "bold")
        )
        titulo.pack(pady=15)

        frame_formulario = tk.Frame(self.tab_ventas)
        frame_formulario.pack(pady=10)

        tk.Label(
            frame_formulario,
            text="Usuario:"
        ).grid(row=0, column=0, padx=10, pady=10)

        self.combo_usuario = ttk.Combobox(
            frame_formulario,
            width=30,
            state="readonly"
        )
        self.combo_usuario.grid(row=0, column=1)

        tk.Label(
            frame_formulario,
            text="Producto:"
        ).grid(row=1, column=0, padx=10, pady=10)

        self.combo_producto = ttk.Combobox(
            frame_formulario,
            width=30,
            state="readonly"
        )
        self.combo_producto.grid(row=1, column=1)

        boton = tk.Button(
            self.tab_ventas,
            text="Registrar venta",
            command=self.callback_registrar_venta
        )
        boton.pack(pady=10)

        columnas = ("usuario", "producto", "fecha")

        self.tabla_ventas = ttk.Treeview(
            self.tab_ventas,
            columns=columnas,
            show="headings"
        )

        self.tabla_ventas.heading("usuario", text="Usuario")
        self.tabla_ventas.heading("producto", text="Producto")
        self.tabla_ventas.heading("fecha", text="Fecha")

        self.tabla_ventas.column("usuario", width=200)
        self.tabla_ventas.column("producto", width=250)
        self.tabla_ventas.column("fecha", width=200)

        self.tabla_ventas.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=15
        )

        self.cargar_datos_ventas()

    def cargar_datos_ventas(self):

        usuarios = self.servicio.obtener_usuarios()
        productos = self.servicio.obtener_productos()

        usuarios_lista = []

        for usuario in usuarios:
            nombre = usuario.get("nombre", usuario.get("usuario", ""))
            usuarios_lista.append(nombre)

        productos_lista = []

        for producto in productos:
            nombre = producto.get("nombre", "")
            productos_lista.append(nombre)

        self.combo_usuario["values"] = usuarios_lista
        self.combo_producto["values"] = productos_lista

        self.actualizar_tabla_ventas()

    def callback_registrar_venta(self):

        usuario = self.combo_usuario.get()
        producto = self.combo_producto.get()

        exito, mensaje = self.servicio.registrar_venta(
            usuario,
            producto
        )

        if exito:
            messagebox.showinfo(
                "Venta",
                mensaje
            )

            self.actualizar_tabla_ventas()

            self.combo_usuario.set("")
            self.combo_producto.set("")

        else:
            messagebox.showwarning(
                "Advertencia",
                mensaje
            )

    def actualizar_tabla_ventas(self):

        for item in self.tabla_ventas.get_children():
            self.tabla_ventas.delete(item)

        ventas = self.servicio.obtener_ventas()

        for venta in ventas:
            self.tabla_ventas.insert(
                "",
                "end",
                values=(
                    venta.get("usuario", ""),
                    venta.get("producto", ""),
                    venta.get("fecha", "")
                )
            )


if __name__ == "__main__":
    root = tk.Tk()
    app = MainView(root)
    root.mainloop()