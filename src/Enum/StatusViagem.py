from enum import Enum

class StatusViagem(Enum):
    PROCURANDO_LOCALIZACAO = 0
    PROCURANDO_MOTORISTA = 1
    AGUARDANDO_CONFIRMACAO_MOTORISTA = 2
    VIAGEM_ANDAMENTO = 3
    VIAGEM_CANCELADA = 4
    VIAGEM_CONCLUIDA = 5
