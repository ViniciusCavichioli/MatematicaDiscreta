
import itertools
class Conjunto():
    def __init__ (self, nome):
        self.elementos = []
        self.nome = nome
        
    def adicionar_Elemento(self,item):
        if isinstance(item, Conjunto):
            self.elementos.append(item)
        else:
            if item not in self.elementos:
                self.elementos.append(item)
                
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
        if (type(conjunto) == Conjunto):    
            for i in conjunto.elementos:
                if i not in self.elementos:
                    return False
            return True

    def eh_subconjunto_proprio(self,conjunto):
        if not self.eh_subconjunto(conjunto):
            return False
        return True
    
    def verifica(self,conjunto):
        if (type(conjunto) == Conjunto):
            return True
        
    def ElementoNeutroE(self,conjunto):
        if len(self.elementos) == 0 and len(conjunto.elementos) != 0:
            return True
        else:
            return False
        
    def ElementoNeutroD(self,conjunto):
        if len(conjunto.elementos) == 0 and len(self.elementos) != 0:
            return True
        else:
            return False
        
    def Idempotencia(self,conjunto):
        if self.elementos == conjunto.elementos:
            return True
        else:
            return False
        
    def RealizaUniao(self, conjunto):
        conjuntoResultado = []
        for i in self.elementos:
            conjuntoResultado.append(i)
        for i in conjunto.elementos:
            if i not in conjuntoResultado:
                conjuntoResultado.append(i)
        return conjuntoResultado
       
    def uniao(self,conjunto):
        if self.ElementoNeutroE(conjunto) == True:
            return print(self.nome,'U',conjunto.nome,'=',self.nome)
        elif self.ElementoNeutroD(conjunto) == True:
            return print(self.nome,'U',conjunto.nome,'=',conjunto.nome)
        elif self.Idempotencia(conjunto) == True:
            return print(self.nome,'U',self.nome,'=',conjunto.nome)
        else:
            result = ""
            verifica = self.RealizaUniao(conjunto)[-1]
            for i in self.RealizaUniao(conjunto):
                if i != verifica:
                    result += str(i) + ","
                else:
                    result += str(i)
            return print(self.nome,"U",conjunto.nome,"= " "{",result,"}")

    def ElementoNeutroI(self,conjunto):
        conjuntoResultado = []
        if conjunto.nome == 'U' or self.nome == 'U':
            for i in self.elementos:
                if i in conjunto.elementos:
                    conjuntoResultado.append(i)
        else:
            return False
        
        if len(conjuntoResultado) == 0:
            return False
        return True
            
    def RealizaInterseccao(self, conjunto):
        conjuntoResultado = []
        for i in self.elementos:
            if i in conjunto.elementos:
                conjuntoResultado.append(i)
        return conjuntoResultado

    def Interseccao(self,conjunto):
        if self.ElementoNeutroI(conjunto) == True:
            if self.nome == 'U':
                return print(self.nome,'∩',conjunto.nome,'=',conjunto.nome)
            else:
                return print(self.nome,'∩',conjunto.nome,'=',self.nome)
        if self.Idempotencia(conjunto) == True:
            return print(self.nome,'∩',self.nome,'=',conjunto.nome)
        else:
            result = ""
            try:
                verifica = self.RealizaInterseccao(conjunto)[-1]
            except:
                print('')
            for i in self.RealizaInterseccao(conjunto):
                if i != verifica:
                    result += str(i) + ","
                else:
                    result += str(i)
            return print(self.nome,"∩",conjunto.nome,"= " "{",result,"}")


    
    def Complemento (self,conjunto):
        conjuntoResultado = []
        for i in self.elementos:
            if i not in conjunto.elementos:
                conjuntoResultado.append(i)
        result = ""
        verifica = conjuntoResultado[-1]
        for i in conjuntoResultado:
            if i != verifica:
                result += str(i) + ","
            else:
                result += str(i)
        return print('~',conjunto.nome,"= " "{",result,"}")           

    def Diferenca(self, conjunto):
        conjuntoResultado = []
        for i in self.elementos:
            if i not in conjunto.elementos:
                conjuntoResultado.append(i)
        result = ""
        verifica = conjuntoResultado[-1]
        for i in conjuntoResultado:
            if i != verifica:
                result += str(i) + ","
            else:
                result += str(i)
        return print(self.nome,'-',conjunto.nome,"= " "{",result,"}") 

    def conjuntoPartes(self):
        conjuntoResultado = []
        tamanhoConjunto = len(self.elementos)
        for x in range(tamanhoConjunto):
            for i in itertools.combinations(self.elementos, x):
                conjuntoResultado.append(i)
        result = ""
        verifica = conjuntoResultado[-1]
        for i in conjuntoResultado:
            if i != verifica:
                result += str(i) + ","
            else:
                result += str(i)
        return print('P(',self.nome,')',"= " "{",result,"}") 


