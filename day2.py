def is_safe(report, dampen=False):
    diffs = []
    for i in range(0, len(report) - 1):
        diffs.append(report[i + 1] - report[i])
    if all(0 < d <= 3 for d in diffs) or all(-3 <= d < 0 for d in diffs):
        return True
    elif dampen:
        for i in range(len(report)):
            if is_safe(report[0:i] + report[i+1:], False):
                return True
    return False


if __name__ == '__main__':
    with open('data/day2.txt', 'r') as file:
        reports = list(map(lambda line: [int(l) for l in line.strip().split()], file))
    print(sum(map(is_safe, reports)))
    print(sum(map(lambda r: is_safe(r, True), reports)))

