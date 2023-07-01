from threading import Thread
from time import sleep

def time_to_await(time_await,thread_exec):
    print(f"Executando thread esperand :{time_await},{thread_exec}")
    sleep(time_await)
    print(f"Encerrando thread {thread_exec}")


def main():
    t1 = Thread(target=time_to_await,args=(3,'t1'))
    t2 = Thread(target=time_to_await,args=(2,'t2'))

    t1.start()
    t2.start()
    t1.join()
    t2.join()

if __name__=='__main__':
    main()