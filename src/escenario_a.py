import random
import matplotlib.pyplot as plt
from graphviz import Digraph
import os

from modelos.proceso import Proceso
from arboles.bst import BST
from arboles.splay_tree import SplayTree

def visualizar_arbol(raiz, nombre_archivo):
    dot = Digraph(comment='BST - Escenario Aleatorio')
    
    def agregar_nodos(nodo, limite=40):
        if nodo is None or limite <= 0:
            return limite
        
        dot.node(str(nodo.proceso.pid), f"PID: {nodo.proceso.pid}\nVR: {nodo.proceso.vruntime:.1f}")
        
        limite -= 1
        if nodo.izquierdo:
            dot.edge(str(nodo.proceso.pid), str(nodo.izquierdo.proceso.pid))
            limite = agregar_nodos(nodo.izquierdo, limite)
        if nodo.derecho:
            dot.edge(str(nodo.proceso.pid), str(nodo.derecho.proceso.pid))
            limite = agregar_nodos(nodo.derecho, limite)
        return limite

    agregar_nodos(raiz)
    ruta_docs = os.path.join(os.path.dirname(__file__), "..", "docs")
    os.makedirs(ruta_docs, exist_ok=True)
    dot.render(os.path.join(ruta_docs, nombre_archivo), format="png", cleanup=True)

def main():
    bst = BST()
    splay = SplayTree()
    procesos_insertados = []
    
    print("Iniciando simulación del Escenario A...")
    
    # Generar 1000 procesos e insertarlos en ambos árboles
    for i in range(1, 1001):
        vruntime = random.uniform(1.0, 1000.0)
        p = Proceso(pid=i, vruntime=vruntime)
        bst.insertar(p)
        splay.insertar(p)
        procesos_insertados.append(p)

    # Crear la imagen del BST con Graphviz
    visualizar_arbol(bst.raiz, "visualizacion_bst_paso4")
    print("[+] Imagen del BST generada en la carpeta docs.")

    # Buscar 100 procesos al azar
    procesos_muestra = random.sample(procesos_insertados, 100)
    iteraciones_bst = []
    iteraciones_splay = []
    
    for p in procesos_muestra:
        _, pasos_b = bst.buscar(p.vruntime)
        iteraciones_bst.append(pasos_b)
        
        _, pasos_s = splay.buscar(p.vruntime)
        iteraciones_splay.append(pasos_s)

    # Gráfica de contraste: Proceso vs Iteraciones
    plt.figure(figsize=(10, 6))
    indices = range(1, 101)
    
    plt.plot(indices, iteraciones_bst, label='BST', marker='o', markersize=4, linestyle='-', alpha=0.8)
    plt.plot(indices, iteraciones_splay, label='Splay Tree', marker='s', markersize=4, linestyle='--', alpha=0.8)
    
    plt.title('Comparativa de Iteraciones por Búsqueda (100 procesos aleatorios)')
    plt.xlabel('Número de Búsqueda (1 a 100)')
    plt.ylabel('Cantidad de Iteraciones')
    plt.legend()
    plt.grid(True, linestyle=':', alpha=0.6)
    
    ruta_graficas = os.path.join(os.path.dirname(__file__), "..", "graficas")
    os.makedirs(ruta_graficas, exist_ok=True)
    plt.savefig(os.path.join(ruta_graficas, "grafica_escenario_a.png"))
    print("[+] Gráfica de iteraciones generada en la carpeta graficas.")
    
    # Mostrar resultados en terminal para copiar a la guía
    avg_bst = sum(iteraciones_bst) / 100
    avg_splay = sum(iteraciones_splay) / 100
    
    print("\n=== RESULTADOS PARA LA GUÍA ===")
    print(f"Promedio BST: {avg_bst:.2f}")
    print(f"Promedio Splay Tree: {avg_splay:.2f}")

main()