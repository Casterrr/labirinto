def pega_prox_pos(lab, pos_y, pos_x, pos_inviaveis, trajeto):
    if pos_y < 0 or pos_x < 0:
       raise Exception('A posição atual não pode ter coordenada negativa!')
    
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
  