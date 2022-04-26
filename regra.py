class Regra():
    def __init__(self, possibilidades):
        self.possibilidades = possibilidades

    def esta_satisfeita(self, atribuicao):
      return True

class UmTimePorRodada(Regra):
  def __init__(self, possibilidades):
    super().__init__(possibilidades)

  def esta_satisfeita(self, atribuicao):
    rodada = list(atribuicao.keys())[-1]
    rodada = rodada[0:2]
    jogos_rodada = [x for x in list(atribuicao.keys()) if x.__contains__(rodada)]
    rodadas = []

    for possibilidade in jogos_rodada:
      times = atribuicao[possibilidade]
      if times is not None:
        time1 = times[0]
        time2 = times[1]
        if (time1 in rodadas or time2 in rodadas):
          return False
        else:
          rodadas.append(time1)
          rodadas.append(time2)
    return True

class UmEstadioPorRodada(Regra):
  def __init__(self,possibilidades):
    super().__init__(possibilidades)

  def esta_satisfeita(self, atribuicao):
    cidades_rodadas = []
    rodada = list(atribuicao.keys())[-1]
    rodada = rodada[0:2]
    jogos_rodada = [x for x in list(atribuicao.keys()) if x.__contains__(rodada)]

    for possibilidade in jogos_rodada:
      times = atribuicao[possibilidade]
      if times is not None:
        time_mandante = times[0]
    
        if (time_mandante["cidade"] in cidades_rodadas):
          return False
        else:
          cidades_rodadas.append(time_mandante["cidade"])
    return True

class UmClassicoPorRodada(Regra):
  def __init__(self,possibilidades):
    super().__init__(possibilidades)

  def esta_satisfeita(self, atribuicao):
    rodada = list(atribuicao.keys())[-1]
    rodada = rodada[0:2]
    jogos_rodada = [x for x in list(atribuicao.keys()) if x.__contains__(rodada)]
    numero_classicos = 0
    
    for possibilidade in jogos_rodada:
      times = atribuicao[possibilidade]
      if times is not None:
        time_um = times[0]
        time_dois = times[1]
      if (time_um["torcedores"] >= 38 and time_dois["torcedores"] >= 38):
        numero_classicos += 1

    if numero_classicos >= 2:
      return False
    else:
      return True