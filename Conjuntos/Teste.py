import Conjunto



A = Conjunto.Conjunto()
A.nome_Conjunto("A")
A.adicionar_Elemento(1)
A.adicionar_Elemento(2)
A.adicionar_Elemento(3)


B = Conjunto.Conjunto()
B.nome_Conjunto("B")
B.adicionar_Elemento(0)



c = Conjunto.Conjunto()

c.nome_Conjunto("C")
c.adicionar_Elemento(1)
c.adicionar_Elemento(2)
c.adicionar_Elemento(2)
c.adicionar_Elemento(2)
c.adicionar_Elemento(5)
c.adicionar_Elemento(10)
c.adicionar_Elemento(3)
c.adicionar_Elemento(11)
c.adicionar_Elemento(3)
c.adicionar_Elemento(9)
c.adicionar_Elemento(A)
c.adicionar_Elemento(B)

print("Listas:")
A.imprimir()
B.imprimir()
c.imprimir()
print()


print("1 pertence a C? ",c.pertence(1))
print("A é subconjunto de C ? ",c.eh_subconjunto(A.elementos))
print("B é subconjunto de C? ",c.eh_subconjunto(B.elementos))
print()
print("A é subconjunto proprio de C? ", c.eh_subconjunto_proprio(A.elementos))
print("B é subconjunto proprio de C? ", c.eh_subconjunto_proprio(B.elementos))



