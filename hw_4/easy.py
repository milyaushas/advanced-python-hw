from time import time
from threading import Thread
from multiprocessing import Process


def fibonacci(n: int) -> [int]:
    if n < 0:
        raise Exception("n must be a non negative integer")
    f = [0, 1]
    for i in range(2, n + 1):
        f.append(f[i - 1] + f[i - 2])
    return f[:n]


def synchronous(n, test_size=10):
    start = time()
    for _ in range(test_size):
        fibonacci(n)
    return time() - start


def threading(n, test_size=10):
    start = time()
    threads = [Thread(target=fibonacci, args=(n,)) for _ in range(test_size)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    return time() - start


def multiprocessing(n, test_size=10):
    start = time()
    processes = [Process(target=fibonacci, args=(n,)) for _ in range(test_size)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    return time() - start


def easy():
    n = 50000
    sync_result = synchronous(n)
    threads_result = threading(n)
    multiprocessing_result = multiprocessing(n)

    with open("artifacts/easy.txt", "w") as file:
        file.write(f"synchronous time: {sync_result} seconds\n")
        file.write(f"threads     time: {threads_result} seconds\n")
        file.write(f"processes   time: {multiprocessing_result} seconds\n")

