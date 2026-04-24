import os
from graphviz import Digraph

from modelos.proceso import Proceso
from arboles.bst import BST
from arboles.splay_tree import SplayTree
from arboles.red_black_tree import RedBlackTree

def visualizar_porcion_bst(raiz, nombre_archivo, limite_nodos=40):
    """
    Genera un gráfico de Graphviz mostrando los primeros nodos del árbol.
    En este escenario ordenado, veremos una línea recta hacia la derecha.
    """
    dot = Digraph(comment='Porción BST Secuencial')
    dot.attr(dpi='300')
    
    def agregar_nodos(nodo, nodos_restantes):
        # Detener la recursión si no hay nodo o si llegamos al límite
        if nodo is None or nodos_restantes <= 0:
            return nodos_restantes
        
        # Etiqueta del nodo con su ID y tiempo de ejecución
        etiqueta = f"PID: {nodo.proceso.pid}\nVR: {nodo.proceso.vruntime}"
        dot.node(str(nodo.proceso.pid), etiqueta)
        
        nodos_restantes -= 1
        
        # Conectar lado izquierdo
        if nodo.izquierdo:
            dot.edge(str(nodo.proceso.pid), str(nodo.izquierdo.proceso.pid))
            nodos_restantes = agregar_nodos(nodo.izquierdo, nodos_restantes)
            
        # Conectar lado derecho
        if nodo.derecho:
            dot.edge(str(nodo.proceso.pid), str(nodo.derecho.proceso.pid))
            nodos_restantes = agregar_nodos(nodo.derecho, nodos_restantes)
            
        return nodos_restantes

    # Iniciar el dibujo desde la raíz
    agregar_nodos(raiz, limite_nodos)
    
    # Asegurar que exista la carpeta docs y guardar la imagen
    ruta_docs = os.path.join(os.path.dirname(__file__), "..", "docs")
    os.makedirs(ruta_docs, exist_ok=True)
    
    ruta_salida = os.path.join(ruta_docs, nombre_archivo)
    dot.render(ruta_salida, format="png", cleanup=True)
    print(f"[+] Imagen generada con éxito en: docs/{nombre_archivo}.png")


def main():
    print("--- PASO 5 (PARTE 1): Llegada Secuencial (Peor Caso) ---")
    
    # Instanciar los tres tipos de árboles
    bst = BST()
    splay = SplayTree()
    rbt = RedBlackTree()
    
    print("1. Insertando 1000 procesos con vruntime ordenado (1 a 1000)...")
    
    # Inserción en orden para forzar el peor escenario en el BST
    for i in range(1, 1001):
        # Se usa el mismo valor para PID y vruntime para simular el orden
        p = Proceso(pid=i, vruntime=float(i))
        bst.insertar(p)
        splay.insertar(p)
        rbt.insertar(p)
        
    print("2. Generando visualización de los primeros 40 nodos del BST...")
    visualizar_porcion_bst(bst.raiz, "paso5_bst_secuencial")
    
    print("3. Buscando el proceso 1000 en las tres estructuras...")
    _, pasos_bst = bst.buscar(1000.0)
    _, pasos_splay = splay.buscar(1000.0)
    _, pasos_rbt = rbt.buscar(1000.0)
    
    # Mostrar resultados en consola para usarlos en el documento
    print("\n" + "="*50)
    print(" RESULTADOS DE BÚSQUEDA DEL ÚLTIMO PROCESO (1000)")
    print("="*50)
    print(f"Iteraciones en BST:            {pasos_bst}")
    print(f"Iteraciones en Splay Tree:     {pasos_splay}")
    print(f"Iteraciones en Red-Black Tree: {pasos_rbt}")
    print("="*50)

main()