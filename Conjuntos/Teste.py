import Conjunto



A = Conjunto.Conjunto("A")
A.adicionar_Elemento(1)
A.adicionar_Elemento(2)
A.adicionar_Elemento(3)
#----------------------------------
B = Conjunto.Conjunto("B")
B.adicionar_Elemento(0)
#----------------------------------
C = Conjunto.Conjunto("C")
C.adicionar_Elemento(1)
C.adicionar_Elemento(2)
C.adicionar_Elemento(2)
C.adicionar_Elemento(2)
C.adicionar_Elemento(5)
C.adicionar_Elemento(10)
C.adicionar_Elemento(3)
C.adicionar_Elemento(11)
C.adicionar_Elemento(3)
C.adicionar_Elemento(9)
C.adicionar_Elemento(A)
C.adicionar_Elemento(B)
#----------------------------------
D = Conjunto.Conjunto("D")
#----------------------------------
U = Conjunto.Conjunto("U")
U.adicionar_Elemento(0)
U.adicionar_Elemento(1)
U.adicionar_Elemento(2)
U.adicionar_Elemento(3)
U.adicionar_Elemento(5)
U.adicionar_Elemento(9)
U.adicionar_Elemento(10)
U.adicionar_Elemento(11)
#----------------------------------
E = Conjunto.Conjunto("E")
E.adicionar_Elemento(5)
E.adicionar_Elemento(9)
E.adicionar_Elemento(10)
E.adicionar_Elemento(11)

print("Listas:")
A.imprimir()
B.imprimir()
C.imprimir()
D.imprimir()
U.imprimir()
print()

print("1 pertence a C? ",C.pertence(1))
print("A é subconjunto de C ? ",C.eh_subconjunto(A))
print("B é subconjunto de C? ",C.eh_subconjunto(B))
print()
print("A é subconjunto proprio de C? ", C.eh_subconjunto_proprio(A))
print("B é subconjunto proprio de C? ", C.eh_subconjunto_proprio(B))

def imprimir2(metodo,nome):
    result = ""
    verifica = metodo[-1]
    for i in metodo:
        if i != verifica:
            result += str(i) + ","
        else:
            result += str(i)
    print(nome, "= " "{",result,"}")
    
imprimir2(U.Complemento(B),'Complemento de B')
imprimir2(U.Diferenca(A),'Diferença de A')
imprimir2(A.conjuntoPartes(),'ConjuntoParte de A')
A.uniao(D)
A.uniao(B)
A.uniao(A)
A.Interseccao(U)
U.Interseccao(A)
U.Interseccao(U)
A.Interseccao(E)
C.Interseccao(A)
A.Interseccao(A)
C.Interseccao(A)

