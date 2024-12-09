from collections import defaultdict


def parse_rules():
    out = defaultdict(lambda: {'before': [], 'after': []})
    with open('data/day5_a.txt', 'r') as f:
        for rule in f:
            before, after = rule.strip().split("|")
            out[before]['before'].append(after)
            out[after]['after'].append(before)
    return out


def parse_updates():
    updates = []
    with open('data/day5_b.txt', 'r') as f:
        for update in f:
            updates.append(update.strip().split(","))
    return updates


def validate_update(update: list[str], rules):
    for i in range(len(update) - 1):
        for j in range(i + 1, len(update)):
            if update[i] in rules[update[j]]['before'] or update[j] in rules[update[i]]['after']:
                return False
    return True


def order_update(update: list[str], rules):
    reordered = [p for p in update]
    while not validate_update(reordered, rules):
        for i in range(len(reordered) - 1):
            modified = False
            for j in range(i + 1, len(reordered)):
                if reordered[i] in rules[reordered[j]]['before'] or reordered[j] in rules[reordered[i]]['after']:
                    reordered.insert(i, reordered.pop(j))
                    modified = True
                    break
            if modified:
                break
    return reordered


if __name__ == '__main__':
    rules = parse_rules()
    middle_sum = 0
    unordered_middle_sum = 0
    for update in parse_updates():
        if validate_update(update, rules):
            middle_sum += int(update[int(len(update) / 2)])
        else:
            ordered = order_update(update, rules)
            unordered_middle_sum += int(ordered[int(len(ordered) / 2)])
    print(middle_sum)
    print(unordered_middle_sum)
