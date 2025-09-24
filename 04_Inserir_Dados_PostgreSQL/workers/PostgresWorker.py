import os
import threading
from queue import Empty
import time
from sqlalchemy import create_engine
from sqlalchemy import text

class PostgresMasterScheduler(threading.Thread):
    def __init__(self,input_queue,**kwargs):
        super(PostgresMasterScheduler,self).__init__(**kwargs)
        self._input_queue = input_queue
        self.start()
    
    def run(self):
        while True:
            try:
                val = self._input_queue.get(timeout=10) # coleta os dados
            except Empty:
                print('Timeout reached in postrgres scheduler, stopping.')
            if val == 'DONE':
                break
            symbol,price,extrated_time = val
            postgresWorker = PostgresWorker(symbol,price,extrated_time) # instancia o executor
            postgresWorker.insert_into_db() # efetua a inserção no banco de dados
        
class PostgresWorker():
    def __init__(self,symbol,price,extrated_time):
        # Instancia os dados obtidos:
        self._symbol = symbol
        self._price = price
        self._extrated_time = extrated_time
        
        # Instancia os dados de conexão com o banco de dados:
        self._PG_USER = os.environ.get('PG_USER','postgres')
        self._PG_PW = os.environ.get('PG_PW','1508')
        self._PG_HOST = os.environ.get('PG_HOST','localhost')
        self._PG_DB = os.environ.get('PG_DB','postgres')
        
        # Cria a engine de conexão com o banco de dados:
        self._engine = create_engine(f'postgresql://{self._PG_USER}:{self._PG_PW}@{self._PG_HOST}/{self._PG_DB}?client_encoding=utf8')
        
    # Cria a query de inserção dos dados:
    def create_insert_query(self):
        SQL = f"INSERT INTO prices (symbol,price,extrated_time) VALUES (:symbol,:price,:extrated_time);"
        return SQL
    
    # Executa a query de inserção dos dados:
    def insert_into_db(self):
        insert_query = self.create_insert_query()
        
        with self._engine.connect() as conn:
            conn.execute(text(insert_query),{
                'symbol': self._symbol,
                'price': self._price,
                'extrated_time': str(self._extrated_time)
            })