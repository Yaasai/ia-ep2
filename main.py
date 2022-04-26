from equipes import equipes
from regra import UmTimePorRodada, UmEstadioPorRodada, UmClassicoPorRodada
from problema import Problema

NUMERO_RODADAS = (len(equipes) - 1) * 2
NUMERO_JOGOS = int(len(equipes) / 2)

jogos = []
for equipe_mandante in equipes:
    for equipe_visitante in equipes:
        if equipe_mandante != equipe_visitante:
            jogos.append((equipe_mandante, equipe_visitante))

if __name__ == "__main__":
    possibilidades = []
    for rodada in range(NUMERO_RODADAS):
        for jogo in range(NUMERO_JOGOS):
            possibilidades.append("R" + str(rodada) + "J" + str(jogo))  

    dominio = {}
    for possibilidade in possibilidades:
        dominio[possibilidade] = jogos

    problema = Problema(possibilidades, dominio)
    problema.adicionar_regra(UmTimePorRodada(possibilidades))
    problema.adicionar_regra(UmEstadioPorRodada(possibilidades))
    problema.adicionar_regra(UmClassicoPorRodada(possibilidades))

    atribuicao_inicial = {}
    resposta = problema.resolver(atribuicao_inicial)

    if resposta is None:
        raise Exception("Nenhuma solução encontrada para o problema")

    for rodada in range(NUMERO_RODADAS):
        print("\n---------- Rodada " + str(rodada + 1) + " ----------\n")
        for jogo in range(NUMERO_JOGOS):
            times = resposta["R" + str(rodada) + "J" + str(jogo)]
            mandante = times[0]
            visitante = times[1]

            print("Jogo " + str(jogo + 1) + ": " + mandante["nome"] + " x " + visitante["nome"] + " | Cidade: " + mandante["cidade"] + "\n")
