# De la carpeta modelos y el archivo 'proceso.py', trae la clase 'Proceso'
from modelos.proceso import Proceso
from modelos.nodo import Nodo

from arboles.bst import BST

def main():
    print("Comenzando prueba de conexión")
    
    # Crear un proceso de prueba
    proceso_prueba = Proceso(pid=1, vruntime=10.5)
    
    # Se crea un nodo con ese proceso
    nodo_prueba = Nodo(proceso=proceso_prueba)
    
    # Se instancia el árbol
    arbol = BST()
    
    print(f"El proceso {nodo_prueba.proceso.pid} tiene un vruntime de {nodo_prueba.proceso.vruntime}")
    print("Los archivos se comunican de forma exitosa")

main()