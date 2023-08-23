from gera_labirinto import gera_lab, print_lab #importa as funções do módulo gera_lab
from pilha import *

def pega_prox_pos(lab, pos_y, pos_x, pos_inviaveis, trajeto):
    if pos_y < 0 or pos_x < 0:
       raise Exception('A posição atual não pode ter coordenada negativa!')
    try:
        # verifica se a casa acima está livre
        if ( 
          (lab[pos_y - 1][pos_x] == ' ') 
          and (pos_y - 1 >= 0) 
          and ( (pos_y - 1, pos_x) not in pos_inviaveis ) 
          and ( not trajeto.includes((pos_y - 1, pos_x)) )
        ):
          return (pos_y - 1, pos_x)
        
        # verifica se a casa à direita está livre
        elif ( 
          (lab[pos_y][pos_x + 1] == ' ') 
          and ( (pos_y, pos_x + 1) not in pos_inviaveis) 
          and ( not trajeto.includes((pos_y, pos_x + 1)) )
        ):
          return (pos_y, pos_x + 1)
        
        # verifica se a casa abaixo está livre
        elif ( 
          (lab[pos_y + 1][pos_x] == ' ') 
          and ( (pos_y + 1, pos_x) not in pos_inviaveis)
          and ( not trajeto.includes((pos_y + 1, pos_x)) )
        ):
          return (pos_y + 1, pos_x)
        
        # verifica se a casa à esquerda está livre
        elif ( 
           (lab[pos_y][pos_x - 1] == ' ') 
           and (pos_x - 1 >= 0) 
           and ( (pos_y, pos_x - 1) not in pos_inviaveis) 
           and ( not trajeto.includes((pos_y, pos_x - 1)) )
        ):
          return (pos_y, pos_x - 1)
        
        # se não houver posição adjacente livre retorna falso
        else:
          return False
    except:
        raise Exception('Alguma posição adjacente não existe na matriz!!!')

m = 7
n = 15
lab = gera_lab(m,n) #gera um labirinto com 7 linhas e 15 colunas
# print_lab(lab) #imprime o lab


m_lab1 = 7
n_lab1 = 15

pos_inicial = (1,0)
pos_final = (m_lab1 - 2, n_lab1 - 1)

labirinto1 = [
  ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'], 
  [' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#'], 
  ['#', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#'], 
  ['#', ' ', '#', '#', ' ', '#', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#'], 
  ['#', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', ' ', ' ', ' ', '#', ' ', '#'], 
  ['#', '#', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#', ' ', ' ', ' '], 
  ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
]

print_lab(lab)

def eh_possivel_sair(lab, pos_inicial, pos_final):
  pos_inviaveis = []

  trajeto = PilhaArray()

  trajeto.push(pos_inicial)
  # posição atual (y,x)
  pos_atual = pos_inicial

  # print(f'pos_final: {pos_final}')
  # print(f'pos_inicial: {pos_inicial}')
  # print(f'pos_atual: {pos_atual}')

  # print(f'pos_inviaveis: {pos_inviaveis}')
  # print(f'trajeto: {trajeto}')

  while True:
    # primeiro de tudo, se a posição atual for igual a posição final, a função já vai retornar verdadeiro.
    if (pos_atual == pos_final):
      return True

    # se a posição atual for igual a posição inicial e houverem posições inviáveis, 
    # significa que ele retornou a posição inicial. Então quebro o loop.
    if (pos_atual == pos_inicial) and len(pos_inviaveis) != 0:
      break
    
    # pega a próxima posição a partir da posição atual
    prox_pos = pega_prox_pos(lab, pos_atual[0], pos_atual[1], pos_inviaveis, trajeto)

    # print(prox_pos)
    # se o valor da próxima posição for válido (uma tupla)
    if (prox_pos):
      trajeto.push(prox_pos)

      pos_atual = prox_pos

      # se a próxima posição já estiver no meu trajeto ou for uma posição inviável, eu anoto que a minha posição atual é inviável 
      # e volto para a minha posição anterior.
    else:
        pos_inviaveis.append(pos_atual)

        

        pos_atual = trajeto.pop()

  return False


print(eh_possivel_sair(lab, pos_inicial, pos_final))
