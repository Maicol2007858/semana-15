# Restaurante App

## Semana 15 - Manejo de eventos

Proyecto de Programación Orientada a Objetos desarrollado con Python y Tkinter.

En esta semana se incorporó el manejo básico de eventos mediante el registro de ventas.

## Funcionalidad implementada

La sección de ventas permite:

* Seleccionar un usuario.
* Seleccionar un producto.
* Registrar una venta.
* Guardar la venta en `ventas.json`.
* Mostrar las ventas en una tabla.
* Recuperar las ventas guardadas al iniciar nuevamente la aplicación.

## Manejo de eventos

El botón **Registrar venta** utiliza `command=` para ejecutar un callback.

El flujo es:

```text
Usuario
   ↓
Botón Registrar venta
   ↓
command=
   ↓
Callback
   ↓
RestauranteServicio
   ↓
ventas.json
   ↓
Tabla de ventas
```

## Estructura

```text
restaurante_app/
├── datos/
├── modelos/
├── servicios/
├── ui/
├── assets/
├── main.py
└── README.md
```

## Persistencia

Las ventas se almacenan en:

`datos/ventas.json`

## Ejecución

Abrir una terminal en la carpeta del proyecto y ejecutar:

```bash
python main.py
```

## Semana 15

Se mantuvo la arquitectura modular del proyecto y se incorporó una operación de venta para demostrar el funcionamiento de eventos, `command=`, callbacks, servicios y persistencia mediante archivos JSON.
