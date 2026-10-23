"""
Boilerplate & Fast I/O - GRCPC 2025
"""
import sys
import os

# Απαραίτητο για βαθύ recursion / DFS / δέντρα (N = 200.000)
sys.setrecursionlimit(300_000)

# Για τοπικό debugging (αν έχεις input.txt)
if os.path.exists('input.txt'):
    sys.stdin = open('input.txt', 'r')

def solve():
    # 1. Για διάβασμα τεράστιου όγκου αριθμών (ΧΩΡΙΣ γραμμές)
    data = sys.stdin.buffer.read().split()
    if not data: return
    it = iter(data)

    n = int(next(it))
    m = int(next(it))

    for _ in range(n):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))

    for i in range(n):
        basic_cost = int(data[i+2])
        congestion_coefficient = int(data[i+2+n])

    # 2. Για κανονικό διάβασμα γραμμή-γραμμή (π.χ. strings ή πίνακες)
    # input = sys.stdin.readline
    # s = input().strip()
    pass


# ==========================================
# Complete Search (Subset Sum / Backtracking)
# ==========================================
def solve_subsets(n, arr):
    total_sum = sum(arr)

    def get_min_diff(index, current_sum):
        # Βάση αναδρομής: Φτάσαμε στο τέλος
        if index == n:
            other_sum = total_sum - current_sum
            return abs(current_sum - other_sum)

        # Επιλογή 1: Παίρνουμε το στοιχείο
        take = get_min_diff(index + 1, current_sum + arr[index])

        # Επιλογή 2: Προσπερνάμε το στοιχείο
        skip = get_min_diff(index + 1, current_sum)

        return min(take, skip)

    return get_min_diff(0, 0)

# ==========================================
# Fast Modular Arithmetic O(log N)
# ==========================================
def fast_power(base, exp):
    MOD = 10**9 + 7
    # Η Python έχει ενσωματωμένο (Fast Modular Exponentiation)
    # Είναι γραμμένο σε C και τρέχει σε O(log exp)
    ans = pow(base, exp, MOD)
    return ans


if __name__ == '__main__':
    solve()