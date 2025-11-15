import sys

# Aumentamos el límite de recursión para QuickSort/MergeSort en listas grandes
sys.setrecursionlimit(10000)

class Algoritmos:
    """
    Clase que contiene los tres algoritmos seleccionados para el estudio.
    Objetivo: Analizar formalmente la complejidad temporal[cite: 13].
    """
    
    @staticmethod
    def bubble_sort(arr):
        # Complejidad Teórica: O(n^2)
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr

    @staticmethod
    def merge_sort(arr):
        # Complejidad Teórica: O(n log n)
        if len(arr) > 1:
            mid = len(arr) // 2
            L = arr[:mid]
            R = arr[mid:]

            Algoritmos.merge_sort(L)
            Algoritmos.merge_sort(R)

            i = j = k = 0
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1

            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1
        return arr

    @staticmethod
    def quick_sort(arr):
        # Complejidad Promedio: O(n log n)
        if len(arr) <= 1:
            return arr
        else:
            pivot = arr[0]
            less = [x for x in arr[1:] if x <= pivot]
            greater = [x for x in arr[1:] if x > pivot]
            return Algoritmos.quick_sort(less) + [pivot] + Algoritmos.quick_sort(greater)
