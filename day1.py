from collections import defaultdict
from typing import List


def read_sorted_input(file_path: str) -> tuple[List[int], List[int]]:
    left_list = []
    right_list = []
    with open(file_path, 'r') as file:
        for line in file:
            l, r = line.strip().split()
            left_list.append(int(l))
            right_list.append(int(r))
    left_list.sort()
    right_list.sort()
    return left_list, right_list


def list_difference(input: List[tuple[int, int]]) -> int:
    return sum(map(lambda x: abs(x[0] - x[1]), input))


def list_similarity_score(left: List[int], right: List[int]) -> int:
    right_count = defaultdict(int)
    for r in right:
        right_count[r] += 1

    return sum([l * right_count[l] for l in left])


if __name__ == '__main__':
    left, right = read_sorted_input('data/day1.txt')
    print(list_difference(list(zip(left, right))))
    print(list_similarity_score(left, right))

