import time

def knapsack_dp(capacity, weights, values, n):
    K = [[0 for x in range(capacity + 1)] for x in range(n + 1)]

    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif weights[i-1] <= w:
                K[i][w] = max(values[i-1] + K[i-1][w-weights[i-1]],  K[i-1][w])
            else:
                K[i][w] = K[i-1][w]

    return K[n][capacity]

if __name__ == '__main__':
    # Case 1: Simple (7 Items)
    v1 = [10, 40, 30, 50, 35, 40, 30]
    w1 = [5, 4, 6, 3, 2, 5, 7]
    c1 = 15
    start = time.time()
    print(f"Case 1 (Simple) Result: {knapsack_dp(c1, w1, v1, len(v1))} | Time: {time.time()-start:.6f}s")

    # Case 2: Medium (20 Items)
    v2 = [ 12, 10, 8, 14, 20, 18, 29, 31, 11, 40, 22,200, 40, 30,35,95,74,7,1,1500]
    w2 = [ 3, 2, 1, 3, 5, 4, 6, 7, 3, 9, 5, 8, 4, 7,2,4,1,4,10,60]
    c2 = 15
    start = time.time()
    print(f"Case 2 (Medium) Result: {knapsack_dp(c2, w2, v2, len(v2))} | Time: {time.time()-start:.6f}s")

    # Case 3: Complex (26 Items)
    v3 = [15, 25, 45, 30, 23, 37, 12, 10, 8, 14, 20, 18, 29, 31, 11, 40, 22,200, 40, 30,35,95,74,7,1,1500]
    w3 = [2, 5, 8, 6, 4, 7, 3, 2, 1, 3, 5, 4, 6, 7, 3, 9, 5, 8, 4, 7,2,4,1,4,10,60]
    c3 = 50
    start = time.time()
    print(f"Case 3 (Complex) Result: {knapsack_dp(c3, w3, v3, len(v3))} | Time: {time.time()-start:.6f}s")