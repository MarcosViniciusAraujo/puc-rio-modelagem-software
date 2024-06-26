import time
from src.Solicitante import Solicitante
from src.Motorista import Motorista

breno = Solicitante(1, 'breno')
breno.cadastrar()

motorista = Motorista(100, 'edmundo')
motorista.cadastrar()

breno.solicitar_corrida('av. dos filhos', 'av. dos filhos', None, 'VIP', 'black')
breno.cancelar_corrida()

time.sleep(5)
motorista.get_nova_corrida()

breno.solicitar_corrida('av. dos filhos', 'av. dos filhos', None, 'VIP', 'black')
time.sleep(5)
motorista.get_nova_corrida()

time.sleep(5)
motorista.finalizar_corrida()

time.sleep(5)
motorista.finalizar_corrida()   