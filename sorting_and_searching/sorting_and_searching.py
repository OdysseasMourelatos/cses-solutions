"""
Sorting & Searching Cheat Sheet - GRCPC 2025
"""
import sys


# ==========================================
# 1. Binary Search on Answer
# ==========================================
def binary_search_on_answer(low, high):
    ans = -1
    while low <= high:
        mid = (low + high) // 2

        if check(mid):  # Το check() υλοποιείται ανάλογα το πρόβλημα
            ans = mid  # Αποθηκεύουμε την έγκυρη απάντηση
            high = mid - 1  # Ή low = mid + 1 (αν ψάχνουμε το μέγιστο)
        else:
            low = mid + 1  # Ή high = mid - 1
    return ans


# ==========================================
# 2. Intervals: Scheduling vs Merging
# ==========================================
def interval_scheduling(intervals):
    # Μέγιστο πλήθος μη-επικαλυπτόμενων διαστημάτων (π.χ. Movie Festival)
    # 1. Ταξινόμηση κατά χρόνο ΛΗΞΗΣ
    intervals.sort(key=lambda x: x[1])
    picks, current_time = 0, 0
    for start, end in intervals:
        if start >= current_time:
            picks += 1
            current_time = end
    return picks


def interval_merging_and_gaps(intervals):
    # Εύρεση κενών (gaps) ή ενώσεις διαστημάτων (π.χ. Foodbreak)
    # 1. Ταξινόμηση κατά χρόνο ΕΝΑΡΞΗΣ
    intervals.sort(key=lambda x: x[0])
    max_end = 0
    max_gap = 0
    for start, end in intervals:
        if start > max_end:
            max_gap = max(max_gap, start - max_end)
        max_end = max(max_end, end)
    return max_gap


# ==========================================
# 3. Sliding Window (Longest subsegment with unique condition)
# ==========================================
def longest_unique_subarray(arr):
    last_seen = {}
    left = 0
    max_len = 0
    for right in range(len(arr)):
        val = arr[right]
        if val in last_seen and last_seen[val] >= left:
            left = last_seen[val] + 1

        last_seen[val] = right
        max_len = max(max_len, right - left + 1)
    return max_len


# ==========================================
# 4. Offline Processing & O(1) Linked List (π.χ. Traffic Lights)
# ==========================================
# Όταν σπάνε διαστήματα ή αφαιρούνται στοιχεία ενδιάμεσα:
# Λύνεται ανάποδα (Reverse Time)! Ξεκινάμε από το τέλος, ΠΡΟΣΘΕΤΟΥΜΕ στοιχεία
# και ενώνουμε γειτονικά κενά χρησιμοποιώντας 2 dictionaries (left_of, right_of).
def reverse_time_linked_list_trick(queries, initial_points):
    left_of, right_of = {}, {}
    # Αρχικοποίηση με τα τελικά σημεία (μετά από όλα τα queries)
    # ... (Σύνδεση: left_of[p] = prev, right_of[p] = next) ...
    #
    # Για κάθε query ΑΝΑΠΟΔΑ:
    # L, R = left_of[p], right_of[p]
    # max_gap = max(max_gap, R - L)
    # right_of[L] = R
    # left_of[R] = L
    pass


# ==========================================
# 5. Difference Array (O(1) Range Updates) [ΝΕΟ & ΧΡΗΣΙΜΟ]
# ==========================================
def difference_array(n, queries):
    # queries: (L, R, X) -> προσθήκη X σε όλα τα στοιχεία από [L, R]
    diff = [0] * (n + 2)  # +2 για ασφάλεια στα όρια

    for L, R, X in queries:
        diff[L] += X
        diff[R + 1] -= X

    # Υπολογισμός τελικού πίνακα με Prefix Sum
    arr = [0] * (n + 1)
    current_val = 0
    for i in range(1, n + 1):
        current_val += diff[i]
        arr[i] = current_val
    return arr


# ==========================================
# 6. Custom Sorting (Python 3) [ΝΕΟ & ΧΡΗΣΙΜΟ]
# ==========================================
from functools import cmp_to_key


def custom_sort_example(arr):
    # Παράδειγμα: Ταξινόμηση strings ώστε να σχηματίζουν τον μέγιστο αριθμό
    def compare(a, b):
        if a + b > b + a:
            return -1  # Το 'a' μπαίνει πριν το 'b'
        elif a + b < b + a:
            return 1
        else:
            return 0

    arr.sort(key=cmp_to_key(compare))
    return arr