import time

class Benchmarking:

    def medir_tiempo(self,tarea,array):
        inicio = time.perf_counter()
        tarea(array)
        fin=time.perf_counter()
        return fin-inicio
    