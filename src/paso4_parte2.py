import random
import matplotlib.pyplot as plt
import os

# Importación de los 3 árboles
from modelos.proceso import Proceso
from arboles.bst import BST
from arboles.splay_tree import SplayTree
from arboles.red_black_tree import RedBlackTree

def main():
    print("--- PASO 4 (PARTE 2): Búsqueda Aleatoria en los 3 Árboles ---")
    
    # Se instancian las tres estructuras
    bst = BST()
    splay = SplayTree()
    rbt = RedBlackTree()
    
    procesos_insertados = []
    
    print("1. Generando 1000 procesos e insertándolos en BST, Splay Tree y Red-Black Tree...")
    # Generar 1000 procesos con vruntimes aleatorios y meterlos en los 3 árboles
    for i in range(1, 1001):
        vruntime = random.uniform(1.0, 1000.0)
        p = Proceso(pid=i, vruntime=vruntime)
        
        bst.insertar(p)
        splay.insertar(p)
        rbt.insertar(p)
        
        procesos_insertados.append(p)

    print("2. Seleccionando 100 procesos al azar para la prueba de búsqueda...")
    # Se eligen 100 procesos que se saben que sí están en el árbol
    procesos_muestra = random.sample(procesos_insertados, 100)
    
    # Listas para guardar cuántas iteraciones tomó cada búsqueda
    iteraciones_bst = []
    iteraciones_splay = []
    iteraciones_rbt = []
    
    print("3. Realizando las búsquedas y contando iteraciones...")
    for p in procesos_muestra:
        # Buscar en BST
        _, pasos_b = bst.buscar(p.vruntime)
        iteraciones_bst.append(pasos_b)
        
        # Buscar en Splay Tree
        _, pasos_s = splay.buscar(p.vruntime)
        iteraciones_splay.append(pasos_s)
        
        # Buscar en Red-Black Tree
        _, pasos_r = rbt.buscar(p.vruntime)
        iteraciones_rbt.append(pasos_r)

    # Generar la gráfica comparativa
    print("4. Generando la gráfica de resultados...")
    plt.figure(figsize=(12, 6))
    indices = range(1, 101) # Eje X: de la búsqueda 1 a la 100
    
    # Se dibujan las 3 líneas con colores y marcadores distintos
    plt.plot(indices, iteraciones_bst, label='BST', marker='o', markersize=4, linestyle='-', alpha=0.7, color='tab:blue')
    plt.plot(indices, iteraciones_splay, label='Splay Tree', marker='s', markersize=4, linestyle='--', alpha=0.7, color='tab:orange')
    plt.plot(indices, iteraciones_rbt, label='Red-Black Tree', marker='^', markersize=4, linestyle='-.', alpha=0.7, color='tab:green')
    
    plt.title('Comparativa de Iteraciones por Búsqueda (100 procesos aleatorios)')
    plt.xlabel('Número de Búsqueda (1 a 100)')
    plt.ylabel('Cantidad de Iteraciones')
    plt.legend()
    plt.grid(True, linestyle=':', alpha=0.6)
    
    # Se guarda la imagen en la carpeta graficas
    ruta_graficas = os.path.join(os.path.dirname(__file__), "..", "graficas")
    os.makedirs(ruta_graficas, exist_ok=True)
    nombre_grafica = "paso4_comparativa_busquedas.png"
    plt.savefig(os.path.join(ruta_graficas, nombre_grafica))
    print(f"[+] Gráfica exportada exitosamente en: graficas/{nombre_grafica}")
    
    # Cálculo de promedios para llenar el PDF
    avg_bst = sum(iteraciones_bst) / 100
    avg_splay = sum(iteraciones_splay) / 100
    avg_rbt = sum(iteraciones_rbt) / 100
    
    print("\n" + "="*50)
    print(" DATOS PARA LLENAR EN LA HOJA DE TRABAJO:")
    print("="*50)
    print(f"Promedio de iteraciones con el BST:            {avg_bst:.2f}")
    print(f"Promedio de iteraciones con el Splay Tree:     {avg_splay:.2f}")
    print(f"Promedio de iteraciones con el Red-Black Tree: {avg_rbt:.2f}")
    print("="*50)

main()