import time

def knapsack_naive(capacity, weights, values, n):
    if n == 0 or capacity == 0:
        return 0

    if weights[n-1] > capacity:
        return knapsack_naive(capacity, weights, values, n-1)
    else:
        return max(
            values[n-1] + knapsack_naive(capacity - weights[n-1], weights, values, n-1),
            knapsack_naive(capacity, weights, values, n-1)
        )

if __name__ == '__main__':
    # Case 1: Simple (7 Items)
    v1 = [10, 40, 30, 50, 35, 40, 30]
    w1 = [5, 4, 6, 3, 2, 5, 7]
    c1 = 15
    start = time.time()
    print(f"Case 1 (Simple) Result: {knapsack_naive(c1, w1, v1, len(v1))} | Time: {time.time()-start:.6f}s")

    # Case 2: Medium (20 Items)
    v2 = [ 12, 10, 8, 14, 20, 18, 29, 31, 11, 40, 22,200, 40, 30,35,95,74,7,1,1500]
    w2 = [ 3, 2, 1, 3, 5, 4, 6, 7, 3, 9, 5, 8, 4, 7,2,4,1,4,10,60]
    c2 = 15
    start = time.time()
    print(f"Case 2 (Medium) Result: {knapsack_naive(c2, w2, v2, len(v2))} | Time: {time.time()-start:.6f}s")

    # Case 3: Complex (26 Items)
    v3 = [15, 25, 45, 30, 23, 37, 12, 10, 8, 14, 20, 18, 29, 31, 11, 40, 22,200, 40, 30,35,95,74,7,1,1500]
    w3 = [2, 5, 8, 6, 4, 7, 3, 2, 1, 3, 5, 4, 6, 7, 3, 9, 5, 8, 4, 7,2,4,1,4,10,60]
    c3 = 50
    start = time.time()
    print(f"Case 3 (Complex) Result: {knapsack_naive(c3, w3, v3, len(v3))} | Time: {time.time()-start:.6f}s")