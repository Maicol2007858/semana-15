from datetime import datetime
from servicios.archivo_servicio import ArchivoServicio


class RestauranteServicio:

    def __init__(self):
        self.archivo = ArchivoServicio()

    def obtener_usuarios(self):
        return self.archivo.leer("usuarios.json")

    def obtener_productos(self):
        return self.archivo.leer("productos.json")

    def obtener_ventas(self):
        return self.archivo.leer("ventas.json")

    def registrar_venta(self, usuario, producto):
        if not usuario:
            return False, "Seleccione un usuario."

        if not producto:
            return False, "Seleccione un producto."

        ventas = self.obtener_ventas()

        nueva_venta = {
            "usuario": usuario,
            "producto": producto,
            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        ventas.append(nueva_venta)

        self.archivo.guardar("ventas.json", ventas)

        return True, "Venta registrada correctamente."

    def validar_login(self, usuario, clave):
        usuarios = self.obtener_usuarios()

        for u in usuarios:
            if u.get("usuario") == usuario and u.get("clave") == clave:
                return True

        return False