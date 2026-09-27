import json
import os


class ArchivoServicio:

    def __init__(self, carpeta="datos"):
        self.carpeta = carpeta

    def _ruta(self, archivo):
        return os.path.join(self.carpeta, archivo)

    def leer(self, archivo):
        ruta = self._ruta(archivo)

        if not os.path.exists(ruta):
            return []

        try:
            with open(ruta, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def guardar(self, archivo, datos):
        os.makedirs(self.carpeta, exist_ok=True)

        ruta = self._ruta(archivo)

        with open(ruta, "w", encoding="utf-8") as f:
            json.dump(datos, f, ensure_ascii=False, indent=4)