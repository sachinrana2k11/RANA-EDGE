import random
import time
from multiprocessing import Process, Queue, Pool,cpu_count, current_process


def put_data(numbers, queue):
    while 1:
        for x in range(10000000):
            data = x
            queue.put(data)
            print("Putting Data-: " + str(data))
            time.sleep(0.001)


def get_data(queue):
    while 1:
        if not queue.empty():
            data = queue.get()
            print("                               Fetching Data-: " + str(data))
            print("                                                                     process used-:" + str(current_process().name))
            print("Queue Size-:"+ str(queue.qsize()))
            time.sleep(0.01)


if __name__ == "__main__":
    q = Queue()
    process_size = cpu_count()
    print(process_size)
    p1 = Process(target=put_data, args=("1", q))
    #p2 = Process(target=get_data, args=("1", q))
    p2 = Pool(process_size,get_data,(q,))
    print(Pool.__sizeof__())
    #p2.map()
    p1.start()
    #p2.start()

    p1.join()
    p2.join()
