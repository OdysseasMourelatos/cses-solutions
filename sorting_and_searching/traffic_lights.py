import sys

def solve():
    input = sys.stdin.readline
    street_len, num_of_lights = map(int, input().split())
    lights = list(map(int, sys.stdin.readline().split()))
    prev_lights = {}
    for i in range(num_of_lights):
        light = lights[i]
        prev_lights[light] = sorted(lights[0:i])

    longest_passages = []
    current_longest_passage_start = 0
    current_longest_passage_end = street_len
    current_longest_passage = current_longest_passage_end - current_longest_passage_start
    for i in range(num_of_lights):
        light = lights[i]
        if light > current_longest_passage_start and light < current_longest_passage_end:
            passage_1, passage_2 = find_passages(i, light, prev_lights[light], street_len)
            current_longest_passage = max(passage_1, passage_2)
            if current_longest_passage_end - light == current_longest_passage:
                current_longest_passage_start = light
            elif light - current_longest_passage_start == current_longest_passage:
                current_longest_passage_end = light
        longest_passages.append(current_longest_passage)

    for passage in longest_passages:
        print(passage, end=" ")


def find_passages(i, light, prev_lights, street_len):
    first_index = 0
    last_index = len(prev_lights) - 1
    if i == 0:
        return light, street_len - light

    while first_index <= last_index:
        middle_index = (first_index + last_index) // 2
        if light < prev_lights[middle_index]:
            last_index = middle_index - 1
        elif light > prev_lights[middle_index]:
            first_index = middle_index + 1

    # 3 cases
    # Last in the list
    if first_index > len(prev_lights) - 1:
        return light - prev_lights[-1], street_len - light
    # First in the list
    elif last_index < 0:
        return light, prev_lights[0] - light
    # In between
    else:
        # LastIndex => left, FirstIndex => Right
        return light - prev_lights[last_index], prev_lights[first_index] - light


if __name__ == '__main__':
    solve()