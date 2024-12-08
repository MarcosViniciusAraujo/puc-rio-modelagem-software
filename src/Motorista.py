import json
from .Corrida import Corrida

class Motorista:

    def __init__(self, _id: str, _nome: str):
        self.id = _id
        self.nome = _nome
        self.corrida_ativa = None
    
    def cadastrar(self):
        motoristas = json.load(open('db/motoristas.json'))
        
        if motoristas.get(self.id) is not None:
            print("Motorista já cadastrado.")
        else:
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
                    
    def finalizar_corrida(self):
        if self.corrida_ativa is None:
            print("Não há corrida ativa para finalizar.")

        try:
            self.corrida_ativa.FinalizaCorrida(self)
            print("Corrida finalizada.")
        except:
            print("Corrida não encontrada.")