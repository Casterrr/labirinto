from gera_labirinto import gera_lab, print_lab #importa as funções do módulo gera_lab
from eh_possivel_sair import *

m = 7
n = 15
lab = gera_lab(m,n) #gera um labirinto com 7 linhas e 15 colunas
# print_lab(lab) #imprime o lab

pos_inicial = (1,0)
pos_final = (m - 2, n - 1)

print_lab(lab)


print(eh_possivel_sair(lab, pos_inicial, pos_final))