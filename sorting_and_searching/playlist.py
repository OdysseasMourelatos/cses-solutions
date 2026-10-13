import sys

def solve():
    n = int(sys.stdin.readline())
    ids = list(map(int, sys.stdin.readline().split()))
    max_streak = 0
    streak_index = 0
    last_seen = {}
    for i in range(n):
        song = ids[i]
        if song in last_seen and last_seen[song] >= streak_index:
            streak_index = last_seen[song] + 1

        last_seen[song] = i
        current_length = i - streak_index + 1
        if current_length > max_streak:
            max_streak = current_length
    print(max_streak)

if __name__ == '__main__':
    solve()