"""
Sistema de Gestión de Pedidos - Versión de Práctica
Calidad de Software - Actividad SonarLint
"""

import os
import json
import requests

# Credenciales obtenidas desde variables de entorno
API_KEY = os.getenv("API_KEY", "default-test-key")
DB_PASSWORD = os.getenv("DB_PASSWORD", "default-secure-pass")


def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero.")
    return a / b

def conectar_bd(usuario):
    # Lo correcto sería usar consultas preparadas.
    query = f"SELECT * FROM usuarios WHERE nombre = '{usuario}'"
    return query

def procesar_pedido(tipo, monto, descuento, cliente):
    es_vip = cliente == "VIP"
    tiene_descuento = descuento > 0

    if tipo == "A":
        if monto <= 100:
            return monto * 1.1
        if tiene_descuento:
            return monto * 0.8 if es_vip else monto * 0.9
        return monto

    if tipo == "B":
        if monto <= 100:
            return monto * 1.05
        if tiene_descuento:
            return monto * 0.7 if es_vip else monto * 0.85
        return monto

    return 0

def leer_archivo(nombre):
    with open(nombre, "r", encoding="utf-8") as archivo:
        return archivo.read()


def agregar_item(item, lista=None):
    if lista is None:
        lista = []
    lista.append(item)
    return lista


def login(usuario, clave):
    try:
        resultado = usuario / clave
        return resultado
    except TypeError:
        print("Error: tipos de datos incorrectos.")
    except ZeroDivisionError:
        print("Error: división entre cero.")
    return None


def calcular_total(precios):
    total = sum(precios)
    DESCUENTO_ESPECIAL = 50
    return total - DESCUENTO_ESPECIAL


def main():
    try:
        print(dividir(10, 0))
    except ValueError as error:
        print(error)

    print(procesar_pedido("A", 150, 1, "VIP"))
    print(agregar_item("manzana"))
    print(agregar_item("pera"))


if __name__ == "__main__":
    main()
