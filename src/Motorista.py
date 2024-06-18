class Motorista:
    id : str
    idade : int
    nome : str
    nota : float
    num_viagens : int
    coordenada : str

    def __init__(self, 
        _id: str, 
        _idade: int, 
        _nome: str, 
        _nota: float, 
        _num_viagens: int, 
        _corrdenada: str):
        
        self.id = _id
        self.idade = _idade
        self.nome = _nome
        self.nota = _nota
        self.num_viagens = _num_viagens
        self.corrdenada = _corrdenada
