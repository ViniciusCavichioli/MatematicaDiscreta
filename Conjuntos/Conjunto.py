class Conjunto():

    def __init__ (self):
        self.elementos = []
        self.tamanho = 0
        self.nome = None

    def nome_Conjunto(self,nome):
        self.nome = nome

    def adicionar_Elemento(self,item):
        if isinstance(item, Conjunto):
            self.elementos.append(item)
        else:
            if item not in self.elementos:
                self.elementos.append(item)
                self.tamanho += 1


    def __str__(self):
        return '{' + ', '.join([str(i) for i in self.elementos]) + '}'

    
    def imprimir(self):
        print(self.nome, "=", self)
        
    def pertence(self,elemento):
        if elemento in self.elementos:
            return True
        else:
            return False
    
    def eh_subconjunto(self,conjunto):
        for i in conjunto:
            if i not in self.elementos:
                return False
        return True
    
    def eh_subconjunto_proprio(self,conjunto):
        for i in conjunto:
            if i not in self.elementos:
                return False
        return True
        for i in self.elementos:
            if i not in conjunto:
                return True
        return False
