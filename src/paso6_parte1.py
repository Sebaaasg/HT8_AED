import random
import matplotlib.pyplot as plt
import os

from modelos.proceso import Proceso
from arboles.splay_tree import SplayTree
from arboles.red_black_tree import RedBlackTree

def main():
    print("--- PASO 6 (PARTE 1): Proceso Frecuente de I/O ---")
    
    # Instanciar los árboles que vamos a comparar
    splay = SplayTree()
    rbt = RedBlackTree()
    procesos_insertados = []
    
    print("1. Generando e insertando 1000 procesos al azar...")
    # Llenar ambos árboles con los mismos datos desordenados
    for i in range(1, 1001):
        vruntime = random.uniform(1.0, 1000.0)
        p = Proceso(pid=i, vruntime=vruntime)
        
        splay.insertar(p)
        rbt.insertar(p)
        procesos_insertados.append(p)

    print("2. Seleccionando un proceso al azar para simular I/O frecuente...")
    # Elegir un solo proceso que buscaremos repetidas veces
    proceso_frecuente = random.choice(procesos_insertados)
    print(f"   -> Proceso seleccionado: PID {proceso_frecuente.pid} (VR: {proceso_frecuente.vruntime:.2f})")

    iteraciones_splay = []
    iteraciones_rbt = []
    
    print("3. Buscando el mismo proceso 50 veces seguidas en ambos árboles...")
    # Simular las 50 búsquedas consecutivas
    for _ in range(50):
        _, pasos_s = splay.buscar(proceso_frecuente.vruntime)
        iteraciones_splay.append(pasos_s)
        
        _, pasos_r = rbt.buscar(proceso_frecuente.vruntime)
        iteraciones_rbt.append(pasos_r)

    print("4. Generando gráfica de contraste...")
    # Configurar el lienzo de la gráfica
    plt.figure(figsize=(10, 6))
    indices = range(1, 51) # Eje X: Búsqueda 1 a la 50
    
    # Trazar las líneas. Usamos marcadores claros para ver el cambio.
    plt.plot(indices, iteraciones_splay, label='Splay Tree', marker='s', linestyle='-', color='tab:orange')
    plt.plot(indices, iteraciones_rbt, label='Red-Black Tree', marker='^', linestyle='--', color='tab:green')
    
    plt.title('Búsqueda Frecuente del Mismo Proceso (Simulación I/O)')
    plt.xlabel('Número de Búsqueda Consecutiva (1 a 50)')
    plt.ylabel('Cantidad de Iteraciones')
    plt.legend()
    
    # Añadir cuadrícula para facilitar la lectura
    plt.grid(True, linestyle=':', alpha=0.6)
    
    # Asegurar que la carpeta graficas exista y guardar la imagen
    ruta_graficas = os.path.join(os.path.dirname(__file__), "..", "graficas")
    os.makedirs(ruta_graficas, exist_ok=True)
    nombre_grafica = "paso6_io_frecuente.png"
    plt.savefig(os.path.join(ruta_graficas, nombre_grafica))
    
    print(f"[+] Gráfica guardada con éxito en: graficas/{nombre_grafica}")
    
    # Calcular promedios para la siguiente parte de la guía
    avg_splay = sum(iteraciones_splay) / 50
    avg_rbt = sum(iteraciones_rbt) / 50
    
    print("\n" + "="*50)
    print(" DATOS PARA LLENAR EN LA HOJA DE TRABAJO:")
    print("="*50)
    print(f"Promedio de iteraciones con Splay Tree:     {avg_splay:.2f}")
    print(f"Promedio de iteraciones con Red-Black Tree: {avg_rbt:.2f}")
    print("="*50)

main()