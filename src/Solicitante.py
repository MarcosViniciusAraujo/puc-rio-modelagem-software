import json
from .Corrida import Corrida
from Enum.StatusViagem import StatusViagem

class Solicitante:
    def __init__(self, _id: int, nome: str):
        self.id = _id
        self.nome = nome
        self.corrida_ativa = None
    
    def cadastrar(self):
        solicitantes = json.load(open('db/solicitantes.json'))
        if solicitantes.get(self.id) is not None:
            raise Exception("Solicitante já cadastrado.")
        
        solicitante = {'nome': self.nome}
        solicitantes[self.id] = solicitante
        
        with open('db/solicitantes.json', 'w') as f:
            json.dump(solicitantes, f, indent=4)

    def solicitar_corrida(self, local_partida, local_destino, paradas, servico, metodo_pagamento):
        corrida = Corrida()
        corrida.buscar(local_partida, local_destino, paradas, servico, metodo_pagamento, self)
        print(f"Corrida solicitada de {local_partida} para {local_destino}.")
        self.corrida_ativa = corrida

    def cancelar_corrida(self):
        if self.corrida_ativa is None:
            raise Exception("Não há corrida ativa para cancelar.")
        
        if self.corrida_ativa.status in (
            StatusViagem.PROCURANDO_LOCALIZACAO, 
            StatusViagem.PROCURANDO_MOTORISTA,
            StatusViagem.AGUARDANDO_CONFIRMACAO_MOTORISTA
            ):
            try:
                self.corrida_ativa.CancelarCorrida(self)
                print("Corrida cancelada.")
            except:
                print("Corrida não encontrada.")
        else:
            print("Corrida não pode ser cancelada.")
        



    
