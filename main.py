import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random
import time

# Importación de algoritmos
from algoritmos import Algoritmos

def plot_results(ax, canvas, sizes, bubble, merge, quick):
    """
    Genera el gráfico comparativo en el canvas existente.
    Recibe 'ax' y 'canvas' como argumentos ya que no son parte de una clase.
    """
    ax.clear()
    
    ax.plot(sizes, bubble, marker='o', label='Bubble Sort (O(n²))', color='red', linestyle='--')
    ax.plot(sizes, merge, marker='s', label='Merge Sort (O(n log n))', color='blue')
    ax.plot(sizes, quick, marker='^', label='Quick Sort (O(n log n))', color='green')

    ax.set_title('Comparación de Complejidad Temporal')
    ax.set_xlabel('Tamaño de la Entrada (N)')
    ax.set_ylabel('Tiempo (segundos)')
    ax.legend()
    ax.grid(True)

    canvas.draw()
    messagebox.showinfo("Éxito", "Análisis completado. Gráfico actualizado.")

def run_analysis(root, entry_widget, ax, canvas):
    """
    Ejecuta la simulación.
    Recibe 'root' (para actualizar la GUI), el widget de entrada, y los objetos de la gráfica.
    """
    try:
        # Parsear tamaños ingresados por el usuario desde el widget pasado como argumento
        sizes_str = entry_widget.get().split(',')
        sizes = [int(s.strip()) for s in sizes_str]
        
        if any(s > 3000 for s in sizes):
            messagebox.showwarning("Advertencia", "Tamaños > 3000 pueden congelar Bubble Sort momentáneamente.")

    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese números válidos separados por comas.")
        return

    # Diccionarios para guardar resultados
    times_bubble = []
    times_merge = []
    times_quick = []

    print("Iniciando simulación...")

    for n in sizes:
        # Generar lista aleatoria
        original_list = [random.randint(0, 10000) for _ in range(n)]
        
        # --- Medir Bubble Sort ---
        arr_copy = original_list.copy()
        start = time.time()
        Algoritmos.bubble_sort(arr_copy)
        end = time.time()
        times_bubble.append(end - start)

        # --- Medir Merge Sort ---
        arr_copy = original_list.copy()
        start = time.time()
        Algoritmos.merge_sort(arr_copy)
        end = time.time()
        times_merge.append(end - start)

        # --- Medir Quick Sort ---
        arr_copy = original_list.copy()
        start = time.time()
        Algoritmos.quick_sort(arr_copy)
        end = time.time()
        times_quick.append(end - start)
        
        # Usamos root.update() en lugar de self.update()
        root.update()

    # Llamamos a la función de graficar pasando los objetos necesarios
    plot_results(ax, canvas, sizes, times_bubble, times_merge, times_quick)

def main():
    # Configuración de la ventana principal
    root = tk.Tk()
    root.title("Taller #2: Complejidad Algorítmica - INFO1148")
    root.geometry("900x700")
    
    # Contenedor principal
    main_frame = ttk.Frame(root, padding="10")
    main_frame.pack(fill=tk.BOTH, expand=True)

    # --- Sección de Configuración ---
    control_frame = ttk.LabelFrame(main_frame, text="Configuración del Experimento", padding="10")
    control_frame.pack(fill=tk.X, pady=5)

    ttk.Label(control_frame, text="Tamaños de lista (separados por coma):").grid(row=0, column=0, padx=5, pady=5)
    
    # Guardamos el entry en una variable local 'sizes_entry'
    sizes_entry = ttk.Entry(control_frame, width=30)
    sizes_entry.insert(0, "100, 500, 1000, 1500, 2000") 
    sizes_entry.grid(row=0, column=1, padx=5, pady=5)

    # --- Sección de Gráficos ---
    graph_frame = ttk.LabelFrame(main_frame, text="Resultados Gráficos", padding="10")
    graph_frame.pack(fill=tk.BOTH, expand=True, pady=5)

    # Inicializar figura de Matplotlib
    figure, ax = plt.subplots(figsize=(6, 4), dpi=100)
    canvas = FigureCanvasTkAgg(figure, master=graph_frame)
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    # --- Botón ---
    # IMPORTANTE: Usamos lambda para pasar los argumentos a la función run_analysis
    btn_run = ttk.Button(
        control_frame, 
        text="Ejecutar Análisis", 
        command=lambda: run_analysis(root, sizes_entry, ax, canvas)
    )
    btn_run.grid(row=0, column=2, padx=10, pady=5)

    # Iniciar loop
    root.mainloop()

if __name__ == "__main__":
    main()