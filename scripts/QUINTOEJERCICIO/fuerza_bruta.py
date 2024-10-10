import sys
import itertools
import time

def main():
    # Verifica que se reciban exactamente 3 argumentos (usuario, contraseña y límite de intentos)
    if len(sys.argv) != 4:
        print("Uso: python fuerza_bruta.py <usuario> <contraseña> <límite_intentos>")
        sys.exit(1)

    # Asigna los argumentos a variables
    usuario = sys.argv[1]
    contrasena = sys.argv[2]
    
    # Intenta convertir el límite de intentos a un entero
    try:
        limite_intentos = int(sys.argv[3])
    except ValueError:
        print("El límite de intentos debe ser un número entero.")
        sys.exit(1)

    # Variables para el ataque de fuerza bruta
    intentos_realizados = 0
    intentos_fallidos = 0
    combinaciones_intentadas = 0  # Contador de combinaciones intentadas
    inicio_sesion = False

    # Caracteres para generar combinaciones
    caracteres = 'abcdefghijklmnopqrstuvwxyz0123456789'

    # Captura el tiempo de inicio
    tiempo_inicio = time.time()

    # Simulación del ataque de fuerza bruta
    for longitud in range(1, len(contrasena) + 1):
        for combinacion in itertools.product(caracteres, repeat=longitud):
            intento = ''.join(combinacion)
            
            # Muestra la combinación actual
            print(f"Intento {intentos_realizados + 1}: Usuario '{usuario}', Contraseña '{intento}'")

            # Comprobamos si se logró iniciar sesión
            if intento == contrasena:
                inicio_sesion = True
                break

            # Aumentamos los contadores de intentos
            intentos_realizados += 1
            intentos_fallidos += 1
            combinaciones_intentadas += 1  

            # Verificamos si se ha alcanzado el límite de intentos
            if intentos_realizados >= limite_intentos:
                print("Se alcanzó el límite de intentos fallidos.")
                break
        if inicio_sesion or intentos_realizados >= limite_intentos:
            break

    tiempo_final = time.time()
    tiempo_total = tiempo_final - tiempo_inicio

    if inicio_sesion:
        print("¡Inicio de sesión exitoso!")
    else:
        print(f"Se alcanzó el límite de intentos fallidos. Total de intentos fallidos: {intentos_fallidos}")

    print(f"Total de combinaciones intentadas: {combinaciones_intentadas}")
    
    print(f"Tiempo total del ataque: {tiempo_total:.2f} segundos")

if __name__ == "__main__":
    main()
