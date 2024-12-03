import re


def part1(text: str) -> int:
    return sum([int(pair[0]) * int(pair[1]) for pair in
                [mul.removeprefix("mul(").removesuffix(")").split(",") for mul in
                 re.findall(r'mul\(\d{1,3},\d{1,3}\)', text)]])


def part2(text: str) -> int:
    return part1("".join(["".join(parts[1:] if i > 0 else parts) for (i, parts) in
                          enumerate([part.split("do()") for part in text.split("don't()")])]))


if __name__ == '__main__':
    with open('data/day3.txt', 'r') as file:
        file_contents = file.read()
        print(part1(file_contents))
        print(part2(file_contents))
