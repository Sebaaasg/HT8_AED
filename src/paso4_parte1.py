import random
import os
from graphviz import Digraph

from modelos.proceso import Proceso
from arboles.bst import BST

def visualizar_porcion_bst(raiz, nombre_archivo, limite_nodos=40):
    """
    Genera un gráfico de Graphviz mostrando solo una porción del árbol
    para que la imagen sea legible en el documento final.
    """
    dot = Digraph(comment='Porción Representativa del BST')
    dot.attr(dpi='300') # Se configura una alta resolución para que se vea bien el PDF
    
    # Función recursiva interna para recorrer el árbol y limitar la cantidad de nodos
    def agregar_nodos(nodo, nodos_restantes):
        if nodo is None or nodos_restantes <= 0:
            return nodos_restantes
        
        # Se dibuja el nodo actual mostrando su PID y su vruntime (con 1 decimal)
        etiqueta = f"PID: {nodo.proceso.pid}\nVR: {nodo.proceso.vruntime:.1f}"
        dot.node(str(nodo.proceso.pid), etiqueta)
        
        nodos_restantes -= 1
        
        # Se conecta con el hijo izquierdo si existe
        if nodo.izquierdo:
            dot.edge(str(nodo.proceso.pid), str(nodo.izquierdo.proceso.pid))
            nodos_restantes = agregar_nodos(nodo.izquierdo, nodos_restantes)
            
        # Se conecta con el hijo derecho si existe
        if nodo.derecho:
            dot.edge(str(nodo.proceso.pid), str(nodo.derecho.proceso.pid))
            nodos_restantes = agregar_nodos(nodo.derecho, nodos_restantes)
            
        return nodos_restantes

    # Se inicia el recorrido desde la raíz
    agregar_nodos(raiz, limite_nodos)
    
    # Se prepara la ruta para guardar la imagen en la carpeta docs/
    ruta_docs = os.path.join(os.path.dirname(__file__), "..", "docs")
    os.makedirs(ruta_docs, exist_ok=True)
    
    ruta_salida = os.path.join(ruta_docs, nombre_archivo)
    dot.render(ruta_salida, format="png", cleanup=True)
    print(f"[+] Imagen generada exitosamente en: docs/{nombre_archivo}.png")

def main():
    print("--- PASO 4 (PARTE 1): Generación y Visualización del BST ---")
    bst = BST()
    
    print("1. Insertando 1000 procesos con vruntime aleatorio...")
    # Generar 1000 procesos emulando llegadas aleatorias
    for i in range(1, 1001):
        vruntime = random.uniform(1.0, 1000.0)
        p = Proceso(pid=i, vruntime=vruntime)
        bst.insertar(p)
        
    print("2. Generando visualización de una porción representativa (40 nodos)...")
    # Llamar a la función para graficar
    visualizar_porcion_bst(bst.raiz, "paso4_bst_aleatorio")
    
    print("¡Proceso terminado! Ya puedes buscar tu imagen en la carpeta docs.")

main()