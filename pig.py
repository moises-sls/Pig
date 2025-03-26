import random as rd

# função para "rolar" um dado
def roll():
    roll = rd.randint(1,6)
    return roll 



# selecionando a quantidade de jogadores
while True:
    players = input("Digite o número de jogadores (2-4): ")
    
    if players.isdigit():               # verificando se o valor do input for um digito numérico:
        
        players = int(players)          # players se torna uma variável tipo int
        
        if 2 <= players <= 4:           # numero de jogadores inserido corretamente
            break
        else:
            print("Deve ser de 2 - 4 jogadores")  # caso o numero de jogadores não seja aceitável
    
    else:                               # resultado do valor não ser de players não ser numérico
        print("Valor inválido.")



# armazenando os scores dos players
max_score = 50
player_scores = [0 for _ in range(players)]     

while max(player_scores) < max_score:
    for player_idx in range(players):
        print("\nTurno do jogador ", player_idx+1, " começando!")
        print("Seu escore total é: ", player_scores[player_idx])
        current_score = 0
        
        while True:
            should_row = input("\nQuer rolar um dado (s)? ")
            if should_row.lower() != "s":                                                    
                break 
            
            value = roll()
            
            if value == 1:
                print("\nVocê rolou 1, perdeu tudo!")
                current_score=0
                break
            else:
                current_score += value
                print("\nVocê rolou um: ", value)
            
            print("Seu escore atual é: ", current_score)
            
        player_scores[player_idx] += current_score     # precisamos += os current_score para o caso do jogador 
                                                       # jogar mais de um turno; se isso não for feito, o score do jogador
                                                       # no turno passado seria substituido pelo novo score, ou seja, se ele 
                                                       # tinha 6 no primeiro turno, finalizou o turno, e no segundo turno 
                                                       # ficou com mais 5, o score final será 5, o qual deveria ser 11.
                    
        print("\nSeu escore final é: ", player_scores[player_idx])



max_score = max(player_scores)
winning_idx = player_scores.index(max_score) # retorna o idx do jogador que obteve o maior valor no jogo
print("Jogador número", winning_idx+1, "ganhou o jogo com um total de:", max_score, "pontos!")


