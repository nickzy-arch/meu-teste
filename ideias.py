import random

personagens = [
    "um robô poeta",
    "uma tartaruga ninja gerente de projetos",
    "um programador sonâmbulo",
    "um dragão gamer",
    "um pirata intergaláctico vendedor de NFTs"
]

locais = [
    "na lua",
    "dentro de um vulcão gelado",
    "no fundo do mar",
    "em Marte",
    "num castelo que anda"
]

missoes = [
    "descobrir um segredo antigo",
    "salvar o universo",
    "fugir do caos",
    "proteger um cristal mágico",
    "dominar o tempo"
]

def gerar_ideia():
    return f"{random.choice(personagens)} precisa {random.choice(missoes)} {random.choice(locais)}."

print(gerar_ideia())
