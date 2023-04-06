import concurrent.futures
import math
from multiprocessing import cpu_count
from time import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from datetime import datetime


def integrate(f, a, b, n_jobs=1, n_iter=1000, cur_job=0):
    start_time = datetime.now()
    acc = 0
    step = (b - a) / n_iter
    n_iter_for_job = n_iter // n_jobs
    start = cur_job * n_iter_for_job
    finish = (cur_job + 1) * n_iter_for_job
    if n_jobs == cur_job:
        finish = n_iter
    for i in range(start, finish):
        acc += f(a + i * step) * step
    time = start_time.strftime("%H:%M:%S:%f %d/%m/%Y")
    logs = f"Job #{cur_job + 1} / {n_jobs} started at {time}\n"
    return acc, logs


def test_integration_with_pool(pool, n_jobs, f=math.cos, a=0, b=math.pi / 2):
    start_time = time()
    futures = []
    logs = ""
    executor = pool(max_workers=n_jobs)
    result = 0
    for i in range(n_jobs):
        futures.append(executor.submit(integrate, f, a, b, n_jobs, 1000, i))
    for f in concurrent.futures.as_completed(futures):
        acc, log = f.result()
        result += acc
        logs += log
    return time() - start_time, logs


def medium():
    cpu_num = cpu_count()
    with open("artifacts/medium.txt", "w") as file:
        for n_jobs in range(1, 2 * cpu_num + 1):
            threads_time, threads_logs = test_integration_with_pool(ThreadPoolExecutor, n_jobs)
            processes_time, processes_logs = test_integration_with_pool(ProcessPoolExecutor, n_jobs)
            file.write(f"N_JOBS = {n_jobs}\n")
            file.write(f"threads   time: {threads_time} seconds\n")
            file.write(f"processes time: {processes_time} seconds\n")
            file.write(f"- - -\nlogs:\n")
            file.write(f"threads:\n{threads_logs}\n")
            file.write(f"processes:\n{processes_logs}")
            file.write("* * *\n\n")