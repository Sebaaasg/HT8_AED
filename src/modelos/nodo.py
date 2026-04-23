class Nodo:
    def __init__(self, proceso):
        self.proceso = proceso
        self.izquierdo = None
        self.derecho = None
        self.padre = None