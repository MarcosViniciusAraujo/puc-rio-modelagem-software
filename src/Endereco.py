class Endereco:
    id: str
    nome: str
    coordenada: str

    def __init__(self, _id: str, _nome: str, _coord: str):
        self.id = _id
        self.nome = _nome
        self.coordenada = _coord
