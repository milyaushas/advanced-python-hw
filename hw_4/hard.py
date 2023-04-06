from multiprocessing import Queue, Pipe
from multiprocessing import Process
from time import sleep
from codecs import encode
import sys
from datetime import datetime

def A(queue, output):
    while True:
        if not queue.empty():
            output.send(queue.get().lower())
            sleep(5)


def B(input, output):
    while True:
        output.send(encode(input.recv(), "rot_13"))


def hard():
    q = Queue()
    A_to_B, B_to_A = Pipe()
    B_to_main, main_to_B = Pipe()
    Process(target=A, args=(q, A_to_B), daemon=True).start()
    Process(target=B, args=(B_to_A, B_to_main), daemon=True).start()

    with open("artifacts/hard.txt", "w") as file:
        while True:
            str = sys.stdin.readline()
            time = datetime.now()
            file.write(f"{time} (input): {str}\n")
            q.put(str)
            result = main_to_B.recv()
            time = datetime.now()
            print(result)
            file.write(f"{time} (output): {result}\n")

