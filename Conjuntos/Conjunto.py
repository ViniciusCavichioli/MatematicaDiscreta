class Conjunto():

    def __init__ (self):
        self.elementos = []
        self.tamanho = 0
        self.nome = None

    def nome_Conjunto(self,nome):
        self.nome = nome

    def adicionar_Elemento(self,item):
        if item not in self.elementos:
            self.elementos.append(item)
            self.tamanho += 1
            
    def imprimir(self):
        result = ""
        verifica = self.elementos[-1]
        for i in self.elementos:
            if i != verifica:
                result += str(i) + ","
            else:
                result += str(i)

        print(self.nome, "= " "{",result,"}")
