from modelos.nodo import Nodo

class BST:
    def __init__(self):
        # La raiz del arbol inicia vacia al crear la estructura
        self.raiz = None
        
    def insertar(self, proceso):
        nuevo_nodo = Nodo(proceso)
        
        # Si el árbol está vacío entonces el nuevo nodo es la raíz
        if self.raiz is None:
            self.raiz = nuevo_nodo
            return
            
        nodo_actual = self.raiz
        while True:
            # Si el vruntime es menor, se va por la rama izquierda
            if proceso.vruntime < nodo_actual.proceso.vruntime:
                if nodo_actual.izquierdo is None:
                    nodo_actual.izquierdo = nuevo_nodo
                    nuevo_nodo.padre = nodo_actual
                    break
                nodo_actual = nodo_actual.izquierdo
                
            # Si el vruntime es mayor o igual, se va por la rama derecha
            else:
                if nodo_actual.derecho is None:
                    nodo_actual.derecho = nuevo_nodo
                    nuevo_nodo.padre = nodo_actual
                    break
                nodo_actual = nodo_actual.derecho
        
    def buscar(self, vruntime):

        # Busca un proceso en el arbol usando su valor de vruntime.
        # Retorna una tupla con dos valores: (El Nodo encontrado o None, La cantidad entera de iteraciones)
        
        nodo_actual = self.raiz
        iteraciones = 0
        
        # Se recorre el arbol hasta encontrar el valor
        while nodo_actual is not None:
            
            # Por cada nodo que vistiado, se suma un paso al contador
            iteraciones += 1 
            
            if vruntime == nodo_actual.proceso.vruntime:
                # Caso exito, se encuentra el proceso, se retorna el nodo y los pasos
                return nodo_actual, iteraciones
                
            elif vruntime < nodo_actual.proceso.vruntime:
                # El valor buscado es menor, se baja por la rama izquierda
                nodo_actual = nodo_actual.izquierdo
                
            else:
                # El valor buscado es mayor, se baja por la rama derecha
                nodo_actual = nodo_actual.derecho
                
        # Caso fallo, donde el bucle termina y no se encontró el valor
        return None, iteraciones