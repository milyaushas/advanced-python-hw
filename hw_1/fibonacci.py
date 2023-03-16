def fibonacci(n: int) -> [int]:
    if n < 0:
        raise Exception("n must be a non negative integer")
    f = [0, 1]
    for i in range(2, n + 1):
        f.append(f[i - 1] + f[i - 2])
    return f[:n]
