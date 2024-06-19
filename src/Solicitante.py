class Solicitante:
    id: str
    nome: str
    idade: int
    coordenada: str
    nota: float

    def __init__(self, _id: str, _nome: str, _idade: int, _coordenada: str, _nota: float):
        self.id = _id
        self.nome = _nome
        self.idade = _idade
        self.coordenada = _coordenada
        self.nota = _nota 
    
    