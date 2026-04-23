class SplayTree:
    def __init__(self):
        # La raiz del arbol inicia vacia al crear la estructura
        self.raiz = None
        
    def splay(self, nodo):
        # Pendiente 
        pass
        
    def insertar(self, proceso):
        # Pendiente 
        pass
        
    def buscar(self, vruntime):
    
        # Busca un proceso en el arbol por su vruntime.
        # Al encontrarlo, se ejecuta la operacion splay para llevar dicho nodo a la raiz.
        # Devuelve: (Nodo encontrado o None, cantidad de iteraciones)
    
        nodo_actual = self.raiz
        iteraciones = 0
        
        while nodo_actual is not None:
            
            # Por cada comparacion, se suma un paso
            iteraciones += 1
            
            if vruntime == nodo_actual.proceso.vruntime:
                # Se encontro el nodo exacto
                # Aqui se llamará a splay (nodo_actual) en el futuro
                return nodo_actual, iteraciones
                
            elif vruntime < nodo_actual.proceso.vruntime:
                # Si se tiene que ir a la izquierda pero no hay nada, se llega al final
                if nodo_actual.izquierdo is None:
                    # se hace splay al ultimo nodo que logramos visitar
                    return None, iteraciones
                
                # Si hay camino, se sigue bajando a la izquierda
                nodo_actual = nodo_actual.izquierdo
                
            else:
                # Si se tiene que ir a la derecha pero no hay nada, llegamos al final
                if nodo_actual.derecho is None:
                    # se hará splay al ultimo nodo que logramos visitar
                    return None, iteraciones
                
                # Si hay camino, se sigue bajando a la derecha
                nodo_actual = nodo_actual.derecho
                
        # Retorno de seguridad por si el arbol esta vacio desde el inicio
        return None, iteraciones