def conversor (tipo_pesos, valor_dolar, pesos):

    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")
    return dolares

menu = """
Bienvenido al Conversor de Monedas 💸

1 - Pesos colombianos. 
2 - Pesos argentinos.
3 - Pesos mexicanos.

Elige una opción: """

opcion = int(input(menu))

if opcion == 1:
    valor_dolar= 3875
    nombre_moneda="colombianos"
elif opcion == 2:
    valor_dolar=65
    nombre_moneda="argentinos"
elif opcion == 3:
    valor_dolar=24
    nombre_moneda="mexicanos"
else:
    print("Ingresa una opción correcta por favor")
pesos = input("¿Cuántos pesos " + nombre_moneda + " tienes?: ")

conversor(nombre_moneda, valor_dolar, pesos)
