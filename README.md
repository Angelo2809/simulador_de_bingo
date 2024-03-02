Bingo Game
Este é um jogo simples de Bingo implementado em Python. O código cria cartelas para vários jogadores, sorteia números, e verifica se algum jogador fez uma linha. O jogo continua até que um jogador faça uma linha.

Funcionalidades
letra_do_numero(numero)
Esta função recebe um número entre 1 e 75 e retorna a letra correspondente (B, I, N, G ou O) de acordo com o intervalo ao qual o número pertence.

sortear_numero(n_base, n_teto, lista_sortidos)
Esta função sorteia um número aleatório entre n_base (inclusive) e n_teto (exclusive), garantindo que o número sorteado não esteja na lista de números já sorteados.

gerar_cartela()
Gera uma cartela de Bingo para um jogador. Cada coluna da cartela representa uma letra (B, I, N, G, O) e contém números aleatórios dentro do intervalo correspondente à letra.

BINGO_linha(cartela)
Verifica se alguma linha foi completada na cartela.

BINGO_cheia(cartela)
Verifica se a cartela está completamente preenchida.

mostrar_cartel(cartela)
Exibe a cartela na forma de matriz transposta.

Execução do Jogo
O jogo é executado para um número específico de jogadores, cada um com um número determinado de cartelas. O sorteio dos números continua até que um jogador complete uma linha. O prêmio é distribuído entre os ganhadores.

Parâmetros do Jogo
quantidade_jogadores: Número total de jogadores.
cartelas_por_jogador: Número de cartelas por jogador.
total_reais: Valor total arrecadado para o prêmio.
premio_linha: Porcentagem do total destinada ao prêmio por linha completada.
Resultado Final
O jogo finaliza quando um jogador completa uma linha. O prêmio é dividido igualmente entre os ganhadores, e as informações sobre os vencedores e prêmios são exibidas.

Divirta-se jogando Bingo! 🎉
