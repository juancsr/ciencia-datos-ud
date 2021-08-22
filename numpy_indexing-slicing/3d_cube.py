"""
Nom: Juan Camilo Sarmiento Reyes
Cod: 20152020067
"""
import numpy as np

num_cub = np.arange(0,729).reshape(9,9,9)
mini_cub = []

def definir_minicub():
    for k in range(3):
        for j in range(3):
            for i in range(3):
                mini_cub.append(num_cub[(k*3):((k*3)+3),(j*3):((j*3)+3),(i*3):((i*3)+3)])

def buscar_minicub(n_index):
    for k in range(9):
        for j in range(9):
            for i in range(9):
                if (mini_cub[n_index][0,0,0] == num_cub[k,j,i]):
                    return [k,j,i]

def mover_minicub(cub_ini,cub_fin):
    pi =  buscar_minicub(cub_ini)
    pf =  buscar_minicub(cub_fin)
    cubo_aux = np.copy(num_cub[pi[0]:(pi[0]+3),pi[1]:(pi[1]+3),pi[2]:(pi[2]+3)])
    cubo_aux2 = num_cub[pf[0]:(pf[0]+3),pf[1]:(pf[1]+3),pf[2]:(pf[2]+3)]
    print("\n\tcubo_aux:\n"+str(cubo_aux))
    num_cub[pi[0]:(pi[0]+3),pi[1]:(pi[1]+3),pi[2]:(pi[2]+3)] = cubo_aux2
    num_cub[pf[0]:(pf[0]+3),pf[1]:(pf[1]+3),pf[2]:(pf[2]+3)] = cubo_aux


definir_minicub()

n = False
while(not n):
    print("CUBOS\n"+str(num_cub))
    b_ini = int(input("\n\tOPCIONES\n¿Cual es el bloque inicial que desea mover?(0-26)\n\t"))
    b_fin = int(input("¿Cual es el bloque con el que desea intercambiar posicion?(0-26)\n\t"))
    mover_minicub(b_ini, b_fin)
    print("\n---------Cubo nuevo--------\n")
    print(num_cub)
    n = bool(input("Oprima tecla enter para continar adicionando cambios.\n\t"))
