from datetime import datetime

class Corrida:
    
    _id: int
    _num_passageiros: int
    _preco_efetivo: float
    _hora_inicio: datetime
    _prev_chegada_destino: datetime
    _gorjeta_motorista: float

    def __init__(self, id: int,
    num_passageiros: int,
    preco_efetivo: float,
    hora_inicio: datetime,
    prev_chegada_destino: datetime,
    gorjeta_motorista: float):
        _id = id
        _num_passgeiros = num_passageiros
        _preco_efetivo = preco_efetivo
        _hora_inicio = hora_inicio
        _prev_chegada_destino = prev_chegada_destino
        _gorjeta_motorista = gorjeta_motorista

    def GetDivisaoPagamento(self):
        pass

    def AvaliaCorrida(self):
        pass

    def CalculaMelhorRota(self):
        pass

    def IniciaCorrida(self):
        pass