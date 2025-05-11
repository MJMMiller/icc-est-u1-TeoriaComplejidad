class SortMethods:

    def burbuja(self, arreglo):
        arreglo = arreglo.copy()
        n = len(arreglo)
        for i in range(n):
            for j in range(0, n-i-1):
                if arreglo[j] > arreglo[j+1]:
                    arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[j]
        return arreglo

    def burbujaMejorado(self, arreglo):
        arreglo = arreglo.copy()
        n = len(arreglo)
        for i in range(n):
            estado = False
            for j in range(n-1-i):
                if arreglo[j] > arreglo[j+1]:
                    arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[j]
                    estado = True
            if not estado:
                break
        return arreglo   

    def seleccion(self, arreglo):
        arreglo = arreglo.copy()
        n = len(arreglo)
        for i in range(n-1):
            ind = i
            for j in range(i+1, n):
                if arreglo[ind] > arreglo[j]:
                    ind = j
            if ind != i:
                arreglo[i], arreglo[ind] = arreglo[ind], arreglo[i]
        return arreglo

    def insercion(self, arreglo):
        arreglo = arreglo.copy()  
        n = len(arreglo)
        for i in range(1, n):
            aux = arreglo[i]
            j = i - 1
            while j >= 0 and arreglo[j] > aux:
                arreglo[j + 1] = arreglo[j]
                j -= 1
            arreglo[j + 1] = aux
        return arreglo 

    def shell(self, arreglo):
        arreglo = arreglo.copy()
        n = len(arreglo)
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                temp = arreglo[i]
                j = i
                while j >= gap and arreglo[j - gap] > temp:
                    arreglo[j] = arreglo[j - gap]
                    j -= gap
                arreglo[j] = temp
            gap //= 2  
        return arreglo
