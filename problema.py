class Problema():
  def __init__(self, possibilidades, dominios):
    self.possibilidades = possibilidades
    self.dominios = dominios
    self.regra = {}

    for possibilidade in self.possibilidades:
        self.regra[possibilidade] = []

  def adicionar_regra(self, regra):
    for possibilidade in regra.possibilidades:
      if possibilidade not in self.possibilidades:
        raise LookupError("Variável não definida previamente")
      else:
        self.regra[possibilidade].append(regra)


  def esta_consistente(self, possibilidade, atribuicao):
    for regra in self.regra[possibilidade]:
      if not regra.esta_satisfeita(atribuicao):
        return False
    return True
  
  def resolver(self, atribuicao):
    if len(atribuicao) == len(self.possibilidades):
      return atribuicao

    possibilidades_nao_atribuida  = [v for v in self.possibilidades if v not in atribuicao]
    primeira_possibilidade = possibilidades_nao_atribuida[0]
    for valor in self.dominios[primeira_possibilidade]:
      if (valor not in atribuicao.values()):
        atribuicao_local = atribuicao.copy()
        atribuicao_local[primeira_possibilidade] = valor
        if self.esta_consistente(primeira_possibilidade, atribuicao_local):
          resultado  = self.resolver(atribuicao_local)
          if resultado is not None:
            return resultado
    return None