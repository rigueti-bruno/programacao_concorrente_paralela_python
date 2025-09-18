import threading
import time

# cria a classe sleep:
class SleepyWorker(threading.Thread):
    # construtor da classe:
    def __init__(self, seconds, **kwargs):
        super(SleepyWorker, self).__init__(**kwargs)  # chama o construtor da superclasse
        self._seconds = seconds  # cria um novo atributo
        self.start()  # inicia o thread

    # método que será a função executada pelo thread:
    def _sleep_a_little(self):
        time.sleep(self._seconds)

    # método run sobrescreve o método run da superclasse Thread e iniciará a execução do thread:
    def run(self):
        self._sleep_a_little()