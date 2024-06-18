from datetime import datetime
from Enum import StatusViagem, TipoServico

import Motorista

class Corrida:
    
    id: str
    num_passageiros: int
    preco_efetivo: float
    hora_inicio: datetime
    prev_chegada_destino: datetime
    gorjeta_motorista: float

    status: StatusViagem
    servico: TipoServico 
    motorista: Motorista
    paradas = []
    solicitantes = []

    def __init__(self, 
    _id: str,
    _num_passageiros: int,
    _preco_efetivo: float,
    _hora_inicio: datetime,
    _prev_chegada_destino: datetime,
    _gorjeta_motorista: float):
        self.id = _id
        self.num_passgeiros = _num_passageiros
        self.preco_efetivo = _preco_efetivo
        self.hora_inicio = _hora_inicio
        self.prev_chegada_destino = _prev_chegada_destino
        self.gorjeta_motorista = _gorjeta_motorista

    def GetDivisaoPagamento(self):
        pass

    def AvaliaCorrida(self):
        pass

    def CalculaMelhorRota(self):
        pass
    
    def atualizaStatus(self, status):
        self.status = status
        print(f'Status = {self.status}')

    def IniciaCorrida(self):
        print('Iniciando corrida...')
        self.atualizaStatus(StatusViagem.PROCURANDO_LOCALIZACAO)

        print('Localização encontrada!')
        self.atualizaStatus(StatusViagem.PROCURANDO_MOTORISTA)

        print('')
