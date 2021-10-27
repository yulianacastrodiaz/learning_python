"""
Script en Python que permita administrar operaciones sobre una lista.
Dentro del programa existirá una lista para almacenar el nombre de distintas frustas. Para el control 
de la lista se mostrará un menú con las opciones:
Agregar
Insertar
Mostrar lista
Buscar una fruta
Eliminar un registro
Ordenar lista
Limpiar lista
Salir
"""

import os

AGREGAR = 1
INSERTAR = 2
MOSTRAR = 3
BUSCAR = 4
ELIMINAR = 5
ORDENAR = 6
LIMPIAR = 7
SALIR = 0

frutas = []


def imprimir_menu():
    os.system("cls")
    print(
        f"""        frutas
  {AGREGAR}) Agregar
  {INSERTAR}) Insertar
  {MOSTRAR}) Mostrar
  {BUSCAR}) Buscar
  {ELIMINAR}) Eliminar
  {ORDENAR}) Ordenar
  {LIMPIAR}) Limpiar
  {SALIR}) Salir"""
    )


def agregar_registro():
    print("         Agregar")
    nombre_fruta = input("Nombre de la fruta: ")
    frutas.append(nombre_fruta)
    print("Registro agregado con éxito.")


def insertar_registro():
    print("         Insertar")
    nombre_fruta = input("Nombre de la fruta: ")
    pos = int(input("Posición: "))
    frutas.insert(pos, nombre_fruta)
    print("Registro insertado en la posición indicada.")


def mostrar_registro():
    print("         Mostrar")
    if len(frutas) > 0:
        for fruta in frutas:
            print(fruta)
    else:
        print("No se han agregado frutas a la lista.")


def buscar_registro():
    print("         Buscar")
    if len(frutas) > 0:
        nombre_fruta = input("Nombre de la fruta a buscar:")
        if nombre_fruta in frutas:
            cantidad = frutas.count(nombre_fruta)
            inicio = 0
            for i in range(cantidad):
                pos = frutas.index(nombre_fruta, inicio)
                print(f"{nombre_fruta} se encuentra en la posición {pos + 1}")
                inicio = pos + 1
        else:
            print(f"{nombre_fruta} no ha sido registrado en la lista")
    else:
        print("No se han agregado frutas a la lista.")


def eliminar_registro():
    print("         Eliminar")
    if len(frutas) > 0:
        for i in range(len(frutas)):
            print(f"{i+1}. {frutas[i]}")
        print("0. Cancelar")
        pos = int(input(f"Índice de la fruta a eliminar (1 - {len(frutas)})"))
        if 0 < pos <= len(frutas):
            frutas.pop(pos - 1)
            print("Registro eliminado con éxito.")
        else:
            print("No se eliminará ningún registro.")
    else:
        print("No se han agregado frutas a la lista.")


def ordenar_registro():
    print("         Ordenar")
    if len(frutas) > 0:
        frutas.sort()
        print("Lista ordenada alfabéticamente.")
    else:
        print("No se han agregado frutas a la lista.")


def limpiar_registro():
    print("         Limpiar")
    frutas.clear()
    print("Los registros han sido borrados.")


def main():
    continuar = True
    while continuar:
        imprimir_menu()
        opc = int(input("Selecciona una opción: "))
        os.system("cls")
        if opc == AGREGAR:
            agregar_registro()
        elif opc == INSERTAR:
            insertar_registro()
        elif opc == MOSTRAR:
            mostrar_registro()
        elif opc == BUSCAR:
            buscar_registro()
        elif opc == ELIMINAR:
            eliminar_registro()
        elif opc == ORDENAR:
            ordenar_registro()
        elif opc == LIMPIAR:
            limpiar_registro()
        elif opc == SALIR:
            print("Nos vemos...")
            continuar = False
        else:
            print("Opción no válida.")
        input("Presiona enter para continuar...")


if __name__ == "__main__":
    main()
