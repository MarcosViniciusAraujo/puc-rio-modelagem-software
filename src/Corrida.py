from datetime import datetime
import json
from re import S
import uuid
from Enum.StatusViagem import StatusViagem


def get_corrida_from_db(id):
        corridas = json.load(open('db/corridas.json'))
        return corridas[id]
class Corrida(): 

    def __init__(self,id=None):
        if not id:
            corrida = {}
        else:
            corrida = get_corrida_from_db(id)

        self.id = id
        self.origem = corrida.get('origem')
        self.destino = corrida.get('destino')
        self.preco_efetivo = corrida.get('preco_efetivo')
        self.hora_inicio = corrida.get('hora_inicio')
        self.prev_chegada_destino = corrida.get('prev_chegada_destino')
        self.gorjeta_motorista = corrida.get('gorjeta_motorista')
        self.status = corrida.get('status')
        self.servico = corrida.get('servico')
        self.motorista = corrida.get('motorista')
        self.paradas = corrida.get('paradas')
        self.solicitantes = corrida.get('solicitantes')
        self.metodo_pagamento = corrida.get('metodo_pagamento')

    
    def get_prev_chegada(self, origem, destino):
        pass
    
    def update_corrida(self):
        corridas = json.load(open('db/corridas.json'))
        corrida_atual = {key: value for key, value in vars(self).items() if key != 'id'}
        corridas[self.id] = corrida_atual
        
        with open('db/corridas.json', 'w') as f:
            json.dump(corridas, f, indent=4)

    def buscar(self, origem, destino, paradas, servico, metodo_pagamento, solicitante):
        print("Buscando motorista...")
        self.id = str(uuid.uuid4())
        self.origem = origem
        self.destino = destino
        self.preco_efetivo = None
        self.hora_inicio = datetime.now()
        self.prev_chegada_destino = self.get_prev_chegada(origem, destino)
        self.gorjeta_motorista = None
        self.status = StatusViagem.PROCURANDO_MOTORISTA   
        self.servico = servico
        self.motorista = None
        self.paradas = paradas
        self.solicitantes = [solicitante]
        self.metodo_pagamento = metodo_pagamento
        self.update_corrida()
    
    def AceitarCorrida(self, motorista):
        print(f"{motorista.nome} aceitou a corrida...")
        if self.status == StatusViagem.PROCURANDO_MOTORISTA:
            self.status = StatusViagem.AGUARDANDO_CONFIRMACAO_MOTORISTA
            self.update_corrida()
        else:
            raise Exception("Não é mais possível aceitar essa corrida.")

    def IniciaCorrida(self, motorista):
        print(f"{motorista.nome} inicou a corrida...")
        self.hora_inicio = datetime.now()   
        self.motorista = motorista     
        self.status = StatusViagem.VIAGEM_ANDAMENTO
        self.update_corrida()

    def FinalizaCorrida(self, motorista):
        print(f"{motorista.nome} inicou a corrida...")
        if self.status == StatusViagem.VIAGEM_ANDAMENTO:
            self.status = StatusViagem.VIAGEM_CONCLUIDA
            self.update_corrida()
        else:
            raise Exception("Corrida precisa estar em andamento para ser finalizada.")
    
    def CancelarCorrida(self, solicitante):
        print(f"{solicitante.nome} cancelau a corrida...")
        if self.status in (StatusViagem.PROCURANDO_LOCALIZACAO, StatusViagem.PROCURANDO_MOTORISTA, StatusViagem.AGUARDANDO_CONFIRMACAO_MOTORISTA):
            self.status = StatusViagem.VIAGEM_CANCELADA
            self.update_corrida()
        else:
            raise Exception("Não é mais possível cancelar essa corrida.")

