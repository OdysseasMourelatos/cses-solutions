# Task: Palindrome Reorder
# Link: https://cses.fi/problemset/task/1755
# Topic: Introductory Problems / Strings (Frequency Map & Construction)
# Complexity: O(N) time, O(N) space

import sys


def solve():
    text = sys.stdin.readline()
    letters = {}
    for letter in text:
        if letter not in letters:
            letters[letter] = 1
        else:
            letters[letter] += 1
    letters.pop('\n', None)

    odd_values = 0
    odd_part = ''
    half_palindrome = []

    for key, value in letters.items():
        if value % 2 != 0:
            odd_values += 1
            odd_part = key * value
        else:
            half_palindrome.append(key * (value // 2))

        if odd_values > 1:
            print("NO SOLUTION")
            return

    left_str = "".join(half_palindrome)
    reversed_text = left_str[::-1]

    print(left_str + odd_part + reversed_text)


if __name__ == '__main__':
    solve()