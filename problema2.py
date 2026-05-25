
def suma_recursiva(lista, pi, pf):
    # caso base
    if pi > pf:
        return 0
    
    return lista[pi] + suma_recursiva(lista, pi + 1, pf)

lista = []
n = int(input("Ingrese el tamaño de la lista: "))

for i in range(n):
    num = int(input(f"Ingrese número {i+1}: "))
    lista.append(num)

print("Lista:", lista)

pi = int(input("Ingrese posición inicial (PI): "))
pf = int(input("Ingrese posición final (PF): "))

resultado = suma_recursiva(lista, pi-1, pf-1)

print("La suma es:", resultado)
     
    
    
    