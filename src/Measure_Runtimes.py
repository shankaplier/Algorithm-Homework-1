import time
from Verifier import run_verifier
import matplotlib.pyplot as plt

sizes = [21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]

def measure_verifier_runtime(input_file, output_file):
    start_time = time.perf_counter()
    run_verifier(input_file, output_file)
    end_time = time.perf_counter()
    print(f"Elapsed time to run verifier and stability checker: {end_time - start_time} seconds")
    return end_time - start_time

def measure_matching_engine_runtime():
    pass

def plot_verifier_runtimes():
    sizes_to_runtime_map = dict()
    for n in sizes:
        elapsed_time = measure_verifier_runtime(f"input_{n}.txt", f"output_{n}.out")
        sizes_to_runtime_map[n] = elapsed_time
        print(f"size: {n}, elapsed time: {elapsed_time} seconds")
    plt.figure(figsize=(10, 6))
    s = list(sizes_to_runtime_map.keys())
    runtimes = list(sizes_to_runtime_map.values())
    plt.plot(s, runtimes, marker='o', linewidth=2)
    plt.xlabel('Input Size (n)')
    plt.ylabel('Runtime (seconds)')
    plt.title('Verifier Runtime vs Input Size')
    plt.grid(True)
    plt.savefig('runtime_plot.png')
    plt.show()

if __name__ == '__main__':
    plot_verifier_runtimes()