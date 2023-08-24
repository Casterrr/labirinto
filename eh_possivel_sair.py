from pilha import *

from pega_prox_pos import *

def eh_possivel_sair(lab, pos_inicial, pos_final):
  pos_inviaveis = []

  trajeto = PilhaArray()

  trajeto.push(pos_inicial)

  # posição atual (y,x)
  pos_atual = pos_inicial

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
