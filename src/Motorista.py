import json
from .Corrida import Corrida

class Motorista:

    def __init__(self, _id: int, _nome: str):
        self.id = _id
        self.nome = _nome
        self.corrida_ativa = None
    
    def cadastrar(self):
        motoristas = json.load(open('db/motoristas.json'))
        if motoristas.get(self.id) is not None:
            raise Exception("Motorista já cadastrado.")
        motorista = {'nome': self.nome}
        motoristas[self.id] = motorista
        
        with open('db/motoristas.json', 'w') as f:
            json.dump(motoristas, f, indent=4)

    def get_nova_corrida(self):
        corridas = json.load(open('db/corridas.json'))
        for id, corrida in corridas.items():
            if corrida['status'] == 'PROCURANDO_MOTORISTA':
                corrida = Corrida(id)
                corrida.IniciaCorrida(self)
                self.corrida_ativa = corrida
                break
            
        print("Não há corridas disponíveis no momento.")
        
    def finalizar_corrida(self):
        if self.corrida_ativa is None:
            raise Exception("Não há corrida ativa para finalizar.")

        try:
            self.corrida_ativa.FinalizaCorrida(self)
            print("Corrida finalizada.")
        except:
            print("Corrida não encontrada.")