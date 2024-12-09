import re


def count_xmas(matrix):
    return sum([len(re.findall(r'(?=(XMAS|SAMX))', row)) for row in matrix])


def reverse(matrix):
    return [row[::-1] for row in matrix]


def rotate(matrix):
    return [''.join([matrix[j][i] for j in range(len(matrix))]) for i in range(len(matrix[0]))]


def rotate_diagonal(matrix):
    output = []
    for i in range(len(matrix)):
        x = 0
        y = i
        row = ''
        while x < len(matrix) and len(matrix[0]) > y >= 0:
            row += matrix[x][y]
            x += 1
            y -= 1
        output.append(row)
    for i in range(1, len(matrix)):
        x = i
        y = len(matrix) - 1
        row = ''
        while x < len(matrix) and len(matrix[0]) > y >= 0:
            row += matrix[x][y]
            x += 1
            y -= 1
        output.append(row)
    return output


def search_form_x_mas(matrix):
    total = 0
    for i in range(1, len(matrix) - 1):
        for j in range(1, len(matrix[0]) - 1):
            if matrix[i][j] == 'A':
                if (matrix[i - 1][j - 1] == 'M' and matrix[i + 1][j + 1] == 'S') or \
                        (matrix[i - 1][j - 1] == 'S' and matrix[i + 1][j + 1] == 'M'):
                    if (matrix[i + 1][j - 1] == 'M' and matrix[i - 1][j + 1] == 'S') or \
                            (matrix[i + 1][j - 1] == 'S' and matrix[i - 1][j + 1] == 'M'):
                        total += 1
    return total


if __name__ == '__main__':
    with open('data/day4.txt', 'r') as file:
        matrix = file.read().split('\n')
        rotated = rotate(matrix)
        diag_1 = rotate_diagonal(matrix)
        diag_2 = rotate_diagonal(reverse(matrix))
        print(
            count_xmas(matrix) +
            count_xmas(rotated) +
            count_xmas(diag_1) +
            count_xmas(diag_2)
        )

        print(search_form_x_mas(matrix))
