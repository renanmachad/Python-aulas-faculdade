from threading import Thread,Lock
from multiprocessing import Process

list = []

def funcao_a(indice):
    for i in range(100000):
        list.append(1)
        print(f"Fim da thread  {indice}")


def main():
    tasks=[]
    for indice in range(10):
        task= Thread(target=funcao_a, args=(indice,))
        tasks.append(task)
        task.start()
    
    print(f"Antes do termino {len(list)}")

    for tarefa in tasks:
        tarefa.join()
    
    print(f" Após o termino {len(list)}")


if __name__=='__main__':
    main()