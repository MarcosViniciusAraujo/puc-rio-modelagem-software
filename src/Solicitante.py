class Solicitante:
    def __init__(self, _id, nome, nota):
        self.id = _id
        self.nome = nome
        self.nota = nota 
        self.logado = False
        self.corrida_ativa = False
        self.local_partida = None
        self.local_destino = None
        self.tipo_viagem = None
        self.metodo_pagamento = None

    def logar(self):
        self.logado = True

    def solicitar_corrida(self, local_partida, local_destino, tipo_viagem, metodo_pagamento):
        if not self.logado:
            raise Exception("Solicitante precisa estar logado para solicitar uma corrida.")
        
        self.local_partida = local_partida
        self.local_destino = local_destino
        self.tipo_viagem = tipo_viagem
        self.metodo_pagamento = metodo_pagamento
        self.corrida_ativa = True
        print(f"Corrida solicitada de {self.local_partida} para {self.local_destino}.")

    def selecionar_metodo_pagamento(self, metodo):
        self.metodo_pagamento = metodo

    def finalizar_corrida(self):
        self.corrida_ativa = False
        print("Corrida finalizada.")

    def dar_nota_motorista(self, nota):
        print(f"Solicitante deu a nota {nota} ao motorista de forma anônima.")

    def cancelar_corrida(self):
        if not self.corrida_ativa:
            raise Exception("Não há corrida ativa para cancelar.")

        self.corrida_ativa = False

    
