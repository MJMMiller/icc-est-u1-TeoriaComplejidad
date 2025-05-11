import random
import time
import matplotlib.pyplot as plt
from sortMethods import SortMethods
from benchMarking import Benchmarking

if __name__=="__main__":

    start_time = time.time()
    
    bench = Benchmarking()
    metodosOr = SortMethods()
    
    tamanios = [ 5000 , 10000 , 30000 , 50000 , 100000 ]
    max_tamanio = max(tamanios)
    
    arreglo_base = []
    
    for i in range(max_tamanio):
        numero = random.randint(0,max_tamanio)
        arreglo_base.append(numero)
    
    resultados = []
    
    def buildArreglo (tamanio):
        return arreglo_base[:tamanio].copy()
    
    
    algoritmos = {
        "Burbuja": metodosOr.burbuja,
        "Burbuja Mejorado": metodosOr.burbujaMejorado,
        "Insercion": metodosOr.insercion,
        "Seleccion": metodosOr.seleccion,
        "Shell": metodosOr.shell
    }

    for tam in tamanios:
        arreglo = buildArreglo(tam)
        for nombre, metodo in algoritmos.items():
            tiempo = bench.medir_tiempo(metodo,arreglo)
            tuplaResultado = (tam,nombre,tiempo)
            resultados.append(tuplaResultado)
    
    for resultado in resultados:
            tam, nombre, tiempo = resultado
            print (f"Metodo: {nombre}, Tamaño: {tam}, Tiempo: {tiempo:.6f} segundos")        
        
    tiempos_by_method ={
        "Burbuja" : [],
        "Burbuja Mejorado":[],
        "Insercion": [],
        "Seleccion": [],
        "Shell": []
    }

    for tam, nombre, tiempo in resultados:
        tiempos_by_method[nombre].append(tiempo)
        
    plt.figure(figsize=(12,8),num="Gráfica comparativa")
    for nombre, tiempo in tiempos_by_method.items():
        plt.plot(tamanios, tiempo, label =nombre,marker='o')
        
    plt.grid()
    plt.title("Comparativa métodos")
    plt.xlabel("Tamaño")
    plt.ylabel("Tiempo")
    plt.legend()
    plt.show()

    end_time = time.time()
    print(f"Tiempo total de ejecución: {end_time - start_time} segundos")