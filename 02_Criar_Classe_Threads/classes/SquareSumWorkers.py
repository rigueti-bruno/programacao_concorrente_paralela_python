import threading
import time

# criando a classe:
class SquareSumWorker(threading.Thread):
    # construtor da classe:
    def __init__(self,n, **kwargs):
        super(SquareSumWorker,self).__init__(**kwargs) # chama o construtor da superclasse
        self._n = n # cria um novo atributo
        self.start() # inicia o thread
        
    # método que será a função executada pelo thread:
    def _calculate_sum_squares(self):
        sum_squares = 0
        for i in range(self._n):
            sum_squares += i ** 2
    
    # método run sobrescreve o método run da superclasse Thread e iniciará a execução do thread:
    def run(self):
        self._calculate_sum_squares()