import random
import time
import numpy as np

def letra_do_numero(numero):
    if numero > 0 and numero <=15:
        return('B')
    elif numero > 15 and numero <=30:
        return('I')
    elif numero > 30 and numero <=45:
        return('N')
    elif numero > 45 and numero <=60:
        return('G')
    elif numero > 60 and numero <=75:
        return('O')
    else:
        raise ValueError(f"Numero fora de escopo - {numero}")



def sortear_numero(n_base, n_teto, lista_sortidos):
    
    numero_sorteado = np.random.randint(n_base, n_teto)
    numero_sorteado = np.random.randint(n_base, n_teto)
    while numero_sorteado in lista_sortidos:
        numero_sorteado = np.random.randint(n_base, n_teto)
    return numero_sorteado




def gerar_cartela():
    random.seed(time.time())
    cartela = [[0] * 5 for _ in range(5)]
    n_base = 1
    n_teto = 15

    for col in range(5):
        sortidos = []
        for i in range(5):
            sortidos.append(sortear_numero(n_base, n_teto, sortidos))
        sortidos.sort()
        for index, numero in enumerate(sortidos):
            cartela[col][index] = numero
        n_base += 15
        n_teto += 15
    cartela[2][2] = 0
    return cartela



def BINGO_linha(cartela):
    # Validar se deu alguma coluna inteira
    for col in range(5):
        acertos = 0
        numeros_acertados = []
        for linha in range(5):
            if (cartela[col][linha] in numeros_ja_sorteados):
                acertos += 1
                numeros_acertados.append(cartela[col][linha])
        if acertos == 5:
            print(f'Venceu com os numeros: {numeros_acertados}')
            return True
        
    # Validar se deu alguma linha inteira
    for linha in range(5):
        acertos = 0
        numeros_acertados = []
        for col in range(5):
            if (cartela[col][linha] in numeros_ja_sorteados):
                acertos += 1
                numeros_acertados.append(cartela[col][linha])
        if acertos == 5:
            print(f'Venceu com os numeros: {numeros_acertados}')
            return True
    
    # Validar se deu a diagonal positiva
    acertos = 0
    numeros_acertados = []
    for x in range(5):
        if (cartela[x][x] in numeros_ja_sorteados):
            acertos += 1
            numeros_acertados.append(cartela[x][x])
    if acertos == 5:
        print(f'Venceu com os numeros: {numeros_acertados}')
        return True
    
    # Validar se deu a diagonal negativa
    acertos = 0
    numeros_acertados = []
    for col, linha in zip(range(4, -1, -1), range(5)):
        if (cartela[col][linha] in numeros_ja_sorteados):
            acertos += 1
            numeros_acertados.append(cartela[col][linha])
    if acertos == 5:
        print(f'Venceu com os numeros: {numeros_acertados}')
        return True
    
    else:
        return False
    

def BINGO_cheia(cartela):
    numeros_cartela = [numero for linha in cartela for numero in linha]
    return all(numero in numeros_ja_sorteados for numero in numeros_cartela)

def mostrar_cartel(cartela):
    matriz_transposta = list(map(list, zip(*cartela)))

    for linha in matriz_transposta:
        print(linha)
########################################################################

numeros_ja_sorteados = [0]
cartelas = []

jogo_rodando = True

quantidade_jogadores = 250
cartelas_por_jogador = 4
n_cartelas = 0
total_reais = 0.5 * quantidade_jogadores * cartelas_por_jogador
premio_linha = total_reais * 0.2
numero_ganhadores = 0
lista_ganhadores = []

# GERAR CARTELAS
for x in range(quantidade_jogadores):
    for jogador in range(cartelas_por_jogador):
        cartelas.append([jogador, gerar_cartela()])
        n_cartelas += 1
        print(f'cartela {n_cartelas} gerada')
        #time.sleep(random.uniform(0.3, 0.6)) # usado para ter maior numero de numeros sortidosDE
        

# Matriz gerada nas condições cartelas[numero do jogador][cartela]
        
while jogo_rodando:
    numero_sorteado = sortear_numero(1, 75, numeros_ja_sorteados)

    print(f'{letra_do_numero(numero_sorteado)} - {numero_sorteado}')
    numeros_ja_sorteados.append(numero_sorteado)

    for cartela in range(n_cartelas):
        if BINGO_linha(cartelas[cartela][1]):
            lista_ganhadores.append([cartela, cartelas[cartela][0]])
            print(f"Cartela {cartela} do jogador {cartelas[cartela][0]}")
            jogo_rodando = False

premio_linha_por_pessoa = premio_linha/len(lista_ganhadores)
print(f'Prêmio total acumulado: R${premio_linha:.2f}')
for n_cartela, jogador in lista_ganhadores:
    print(f'o jogador {jogador} fez a linha na cartela {n_cartela} e levou o prêmio de R${premio_linha_por_pessoa:.2f}')
print(f"Jogo finalizado com {len(numeros_ja_sorteados)} numeros sorteados")

