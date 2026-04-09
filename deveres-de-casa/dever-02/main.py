
import time


def fatorial(n):

    if n <= 1:
        return 1
  
    return n * fatorial(n - 1)


for n in [10, 100, 500, 1000]:
    inicio = time.perf_counter()
    resultado = fatorial(n)
    fim = time.perf_counter()
    print(f"n={n}: {(fim-inicio)*1e6:.4f} µs")
