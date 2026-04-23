from modelos.nodo import Nodo

class SplayTree:
    def __init__(self):
        self.raiz = None

    def rotar_derecha(self, x):
        y = x.izquierdo
        x.izquierdo = y.derecho
        if y.derecho is not None:
            y.derecho.padre = x
        y.padre = x.padre
        if x.padre is None:
            self.raiz = y
        elif x == x.padre.derecho:
            x.padre.derecho = y
        else:
            x.padre.izquierdo = y
        y.derecho = x
        x.padre = y

    def rotar_izquierda(self, x):
        y = x.derecho
        x.derecho = y.izquierdo
        if y.izquierdo is not None:
            y.izquierdo.padre = x
        y.padre = x.padre
        if x.padre is None:
            self.raiz = y
        elif x == x.padre.izquierdo:
            x.padre.izquierdo = y
        else:
            x.padre.derecho = y
        y.izquierdo = x
        x.padre = y

    def splay(self, n):
        while n.padre is not None:
            if n.padre.padre is None:
                if n == n.padre.izquierdo:
                    self.rotar_derecha(n.padre)
                else:
                    self.rotar_izquierda(n.padre)
            elif n == n.padre.izquierdo and n.padre == n.padre.padre.izquierdo:
                self.rotar_derecha(n.padre.padre)
                self.rotar_derecha(n.padre)
            elif n == n.padre.derecho and n.padre == n.padre.padre.derecho:
                self.rotar_izquierda(n.padre.padre)
                self.rotar_izquierda(n.padre)
            elif n == n.padre.derecho and n.padre == n.padre.padre.izquierdo:
                self.rotar_izquierda(n.padre)
                self.rotar_derecha(n.padre)
            else:
                self.rotar_derecha(n.padre)
                self.rotar_izquierda(n.padre)

    def insertar(self, proceso):
        nuevo_nodo = Nodo(proceso)
        y = None
        x = self.raiz

        while x is not None:
            y = x
            if nuevo_nodo.proceso.vruntime < x.proceso.vruntime:
                x = x.izquierdo
            else:
                x = x.derecho

        nuevo_nodo.padre = y
        if y is None:
            self.raiz = nuevo_nodo
        elif nuevo_nodo.proceso.vruntime < y.proceso.vruntime:
            y.izquierdo = nuevo_nodo
        else:
            y.derecho = nuevo_nodo

        self.splay(nuevo_nodo)

    def buscar(self, vruntime):
        nodo_actual = self.raiz
        iteraciones = 0
        ultimo_visitado = None

        while nodo_actual is not None:
            iteraciones += 1
            ultimo_visitado = nodo_actual
            if vruntime == nodo_actual.proceso.vruntime:
                self.splay(nodo_actual)
                return nodo_actual, iteraciones
            elif vruntime < nodo_actual.proceso.vruntime:
                nodo_actual = nodo_actual.izquierdo
            else:
                nodo_actual = nodo_actual.derecho

        if ultimo_visitado is not None:
            self.splay(ultimo_visitado)
        return None, iteraciones