from modelos.nodo import Nodo
from modelos.proceso import Proceso

class RedBlackTree:
    def __init__(self):
        # Para el Red-Black Tree, se usa un Nodo Fantasma (NIL) en lugar de None
        # Esto evita errores de referencia y facilita la lógica de colores
        proceso_nulo = Proceso(pid=-1, vruntime=0) 
        self.NodoFantasma = Nodo(proceso_nulo)
        self.NodoFantasma.color = 0 # 0 = Negro 1 = Rojo
        self.raiz = self.NodoFantasma

    def rotar_izquierda(self, x):
        y = x.derecho
        x.derecho = y.izquierdo
        if y.izquierdo != self.NodoFantasma:
            y.izquierdo.padre = x
        y.padre = x.padre
        if x.padre == None:
            self.raiz = y
        elif x == x.padre.izquierdo:
            x.padre.izquierdo = y
        else:
            x.padre.derecho = y
        y.izquierdo = x
        x.padre = y

    def rotar_derecha(self, y):
        x = y.izquierdo
        y.izquierdo = x.derecho
        if x.derecho != self.NodoFantasma:
            x.derecho.padre = y
        x.padre = y.padre
        if y.padre == None:
            self.raiz = x
        elif y == y.padre.derecho:
            y.padre.derecho = x
        else:
            y.padre.izquierdo = x
        x.derecho = y
        y.padre = x
    
    def arreglar(self, k):
        # Mientras mi padre sea Rojo
        while k.padre != None and k.padre.color == 1: 
            if k.padre == k.padre.padre.izquierdo:
                u = k.padre.padre.derecho # Mi tío
                if u != None and u.color == 1: # CASO 1: Mi Tío es Rojo
                    u.color = 0
                    k.padre.color = 0
                    k.padre.padre.color = 1
                    k = k.padre.padre # se sigue revisando al abuelo
                else:
                    if k == k.padre.derecho: # CASO 2: Triángulo
                        k = k.padre
                        self.rotar_izquierda(k)
                    # CASO 3: Línea
                    k.padre.color = 0
                    k.padre.padre.color = 1
                    self.rotar_derecha(k.padre.padre)
            else: # Simetría, el padre es hijo derecho
                u = k.padre.padre.izquierdo # Mi tío
                if u != None and u.color == 1: # CASO 1: Mi Tío es Rojo
                    u.color = 0
                    k.padre.color = 0
                    k.padre.padre.color = 1
                    k = k.padre.padre
                else:
                    if k == k.padre.izquierdo: # CASO 2: Triángulo
                        k = k.padre
                        self.rotar_derecha(k)
                    # CASO 3: Línea
                    k.padre.color = 0
                    k.padre.padre.color = 1
                    self.rotar_izquierda(k.padre.padre)
            
            if k == self.raiz:
                break
        self.raiz.color = 0 # Raíz siempre Negra

    def insertar(self, proceso):
        # 1) Inserción normal como BST
        nuevo_nodo = Nodo(proceso)
        nuevo_nodo.padre = None
        nuevo_nodo.izquierdo = self.NodoFantasma
        nuevo_nodo.derecho = self.NodoFantasma
        nuevo_nodo.color = 1 # Los nodos nuevos siempre entran como Rojos

        padre = None
        actual = self.raiz

        while actual != self.NodoFantasma:
            padre = actual
            if nuevo_nodo.proceso.vruntime < actual.proceso.vruntime:
                actual = actual.izquierdo
            else:
                actual = actual.derecho

        nuevo_nodo.padre = padre
        if padre == None:
            self.raiz = nuevo_nodo
        elif nuevo_nodo.proceso.vruntime < padre.proceso.vruntime:
            padre.izquierdo = nuevo_nodo
        else:
            padre.derecho = nuevo_nodo

        # Si es la raíz debe quedar negra
        if nuevo_nodo.padre == None:
            nuevo_nodo.color = 0
            return

        # Si no hay abuelo, no hay nada que arreglar
        if nuevo_nodo.padre.padre == None:
            return

        # 2) Reparar propiedades rojo-negro
        self.arreglar(nuevo_nodo)

    def buscar(self, vruntime):
        """
        Busca un proceso en el árbol usando su valor de vruntime.
        Retorna una tupla con dos valores: (El Nodo encontrado o None, La cantidad entera de iteraciones)
        """
        actual = self.raiz
        iteraciones = 0

        while actual != self.NodoFantasma:
            iteraciones += 1

            if vruntime == actual.proceso.vruntime:
                return actual, iteraciones

            if vruntime < actual.proceso.vruntime:
                actual = actual.izquierdo
            else:
                actual = actual.derecho

        # Retorna None y los pasos si no lo encuentra
        return None, iteraciones