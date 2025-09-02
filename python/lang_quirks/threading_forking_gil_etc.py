#!/usr/bin/env python3
"""
Demonstrates how multiprocessing can avoid GIL restrictions
while threading cannot for CPU-bound tasks.
"""

import time
import multiprocessing
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def cpu_bound_task(n):
    """A CPU-intensive task that will be limited by the GIL in threading."""
    result = 0
    for i in range(n):
        result += i**2
    return result


def benchmark_sequential(tasks):
    """Run tasks sequentially."""
    print("Running sequentially...")
    start_time = time.time()
    results = [cpu_bound_task(task) for task in tasks]
    end_time = time.time()
    print(f"Sequential execution took: {end_time - start_time:.2f} seconds")
    return results


def benchmark_threading(tasks):
    """Run tasks using threading (GIL-limited)."""
    print("Running with threading...")
    start_time = time.time()
    with ThreadPoolExecutor(max_workers=4) as executor:
        results = list(executor.map(cpu_bound_task, tasks))
    end_time = time.time()
    print(f"Threading execution took: {end_time - start_time:.2f} seconds")
    return results


def benchmark_multiprocessing(tasks):
    """Run tasks using multiprocessing (GIL-free)."""
    print("Running with multiprocessing...")
    start_time = time.time()
    with ProcessPoolExecutor(max_workers=4) as executor:
        results = list(executor.map(cpu_bound_task, tasks))
    end_time = time.time()
    print(f"Multiprocessing execution took: {end_time - start_time:.2f} seconds")
    return results


def demonstrate_gil_avoidance():
    """Compare performance between threading and multiprocessing."""
    # CPU-bound tasks that will show the GIL limitation
    tasks = [1000000] * 4  # 4 tasks, each calculating sum of squares up to 1M

    print("=" * 60)
    print("Demonstrating GIL limitations and multiprocessing benefits")
    print("=" * 60)

    # Sequential baseline
    benchmark_sequential(tasks)
    print()

    # Threading (limited by GIL)
    benchmark_threading(tasks)
    print()

    # Multiprocessing (avoids GIL)
    benchmark_multiprocessing(tasks)
    print()

    print("Key observations:")
    print("- Sequential: Baseline performance")
    print("- Threading: Similar to sequential (GIL prevents parallelism)")
    print("- Multiprocessing: Significant speedup (no GIL)")


def worker_with_queue(queue, worker_id):
    result = cpu_bound_task(100000)
    queue.put(f"Worker {worker_id}: {result}")


def multiprocessing_communication_example():
    """Show different ways processes can communicate."""
    print("=" * 60)
    print("Multiprocessing communication methods")
    print("=" * 60)

    print("1. Using Queue for communication:")
    queue = multiprocessing.Queue()
    processes = []

    for i in range(3):
        p = multiprocessing.Process(target=worker_with_queue, args=(queue, i))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    while not queue.empty():
        print(f"   {queue.get()}")

    print()

    print("2. Using Pool with return values:")
    with multiprocessing.Pool(processes=3) as pool:
        tasks = [50000, 75000, 100000]
        results = pool.map(cpu_bound_task, tasks)
        for i, result in enumerate(results):
            print(f"   Task {i}: {result}")


def gil_vs_multiprocessing_tradeoffs():
    """Discuss when to use threading vs multiprocessing."""
    print("=" * 60)
    print("Threading vs Multiprocessing Trade-offs")
    print("=" * 60)

    print("Use THREADING when:")
    print("- I/O-bound tasks (file/network operations)")
    print("- Tasks that release the GIL (NumPy, C extensions)")
    print("- Need shared memory between threads")
    print("- Lower overhead required")
    print()

    print("Use MULTIPROCESSING when:")
    print("- CPU-bound tasks in pure Python")
    print("- Need true parallelism")
    print("- Tasks are independent")
    print("- Can afford process creation overhead")
    print()

    print("LIMITATIONS of multiprocessing:")
    print("- Higher memory usage (separate processes)")
    print("- Slower startup time")
    print("- More complex data sharing")
    print("- Serialization overhead for data transfer")


if __name__ == "__main__":
    # Set start method for compatibility
    multiprocessing.set_start_method("spawn", force=True)

    demonstrate_gil_avoidance()
    print()
    multiprocessing_communication_example()
    print()
    gil_vs_multiprocessing_tradeoffs()
