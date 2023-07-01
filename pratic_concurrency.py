from threading import Thread
from time import sleep


def await_time(sleep_time,mensagem):
    print(f"Inicio tarefa {mensagem}")
    sleep(sleep_time)
    print(f"fim tarefa {mensagem}")


def main():
 
    tarefa= Thread(target=await_time,args=(2,'Thread em execução'))
    tarefa.start()
    print("executando tarefa")
    tarefa.join()
    print("execução concluida")
   
    




if __name__ =='__main__':
    main()