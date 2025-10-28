import json
import urllib.request
import time
from threading import Thread

finished_count = 0 # cria um contador para as threads finalizadas

# função que baixa o conteúdo da web e conta as letras:
def count_letters(url, frequency):
    response = urllib.request.urlopen(url) # faz o dounload do conteudo da web
    txt = str(response.read()) # converte o conteudo para string
    for l in txt: # itera no conteudo baixado
        letter = l.lower() # converte a letra para minuscula
        if letter in frequency:
            frequency[letter] += 1 # incrementa a contagem da letra em 1
    global finished_count
    finished_count += 1 # incrementa o contador de threads finalizadas
    return frequency

def main():
    frequency = {} # dicionario para armazenar a frequencia das letras
    for c in 'abcdefghijklmnopqrstuvwxyz':
        frequency[c] = 0 # inicializa a contagem de cada letra com 0
    
    start = time.time() # marca o tempo de inicio
    for i in range(1000,1020):
        # encapsula a chamada da funcao em uma thread
        Thread(target=count_letters, args=(f"https://www.rfc-editor.org/rfc/rfc{i}.txt", frequency)).start() # conta as letras dos documentos RFC 1000 a 1019
    while finished_count < 20:
        time.sleep(0.5) # aguarda um pouco antes de verificar novamente
    end = time.time() # marca o tempo de fim
    
    print(json.dumps(frequency, indent=4)) # imprime a frequencia das letras em formato JSON
    print(f"Tempo gasto: {end - start} segundos") # imprime o tempo gasto
    

main() # executa a funcao main se o script for executado diretamente