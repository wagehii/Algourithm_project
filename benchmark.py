import time
import random
import csv
# بنستدعي الدوال من الملفات اللي عملناها قبل كده
# تأكد إن ملفات algorithm1.py و algorithm2.py موجودة جنب الملف ده
from algorithm1 import knapsack_naive
from algorithm2 import knapsack_dp

def generate_random_data(n):
    """Generate random weights and values for n items."""
    weights = [random.randint(1, 10) for _ in range(n)]
    values = [random.randint(10, 100) for _ in range(n)]
    capacity = n * 5  
    return capacity, weights, values

def run_benchmark():
    results = []
    print("Running Benchmark... Please wait (This might take a few seconds)...\n")
    
    header = ["n(Input Size)", "Naive Time(sec)", "Optimized Time(sec)","Naive output","Optimized output"]
    print("  ,  ".join(header))
    
    test_sizes = [3, 5, 10, 15, 18, 20, 21, 22  ] 

    for n in test_sizes:
        capacity, weights, values = generate_random_data(n)
        
        start_time = time.time()
        navie_out = knapsack_naive(capacity, weights, values, n)
        naive_duration = time.time() - start_time
        
        start_time = time.time()
        opt_out = knapsack_dp(capacity, weights, values, n)
        opt_duration = time.time() - start_time
        
        print(f"{n}         ,       {naive_duration:.6f}         ,      {opt_duration:.6f}         ,      {navie_out}         ,      {opt_out}")

    print("\n--- Bonus Test for Optimized Only (Large Inputs) ---")
    print("n(Input Size)  ,  Optimized Time (sec)")
    for n in [50, 100, 200, 500]:
        capacity, weights, values = generate_random_data(n)
        start_time = time.time()
        knapsack_dp(capacity, weights, values, n)
        opt_duration = time.time() - start_time
        print(f"{n}              ,  {opt_duration:.6f}             ")

if __name__ == '__main__':
    run_benchmark()