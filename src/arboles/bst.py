class BST:
    def __init__(self):
        # La raiz del arbol inicia vacia al crear la estructura
        self.raiz = None
        
    def insertar(self, proceso):
        # Pendiente
        pass
        
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