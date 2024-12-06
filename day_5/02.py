from collections import defaultdict
from functools import cmp_to_key

def parse_input(rules, updates):
    """
    Parses the rules and updates from the input.

    :param rules: List of rules in the format "X|Y".
    :param updates: List of updates as strings of comma-separated page numbers.
    :return: A tuple of (rules_dict, updates_list).
    """
    rules_dict = defaultdict(list)
    for rule in rules:
        x, y = map(int, rule.split('|'))
        rules_dict[y].append(x)

    updates_list = [list(map(int, update.split(','))) for update in updates]
    return rules_dict, updates_list

def is_update_correct(rules_dict, update):
    page_positions = {page: idx for idx, page in enumerate(update)}

    for y, x_list in rules_dict.items():
        if y in page_positions:
            for x in x_list:
                if x in page_positions and page_positions[x] > page_positions[y]:
                    return False
    return True

def reorder_update(rules_dict, update):
    def compare(x, y):
        if y in rules_dict[x]:
            return -1
        if x in rules_dict[y]:
            return 1
        return 0

    return sorted(update, key=cmp_to_key(compare))

def find_middle_page(update):
    return update[len(update) // 2]

def main():
    rules = []
    updates = []
    with open('day_5/01.txt') as f:
        data = f.read().splitlines()
        for line in data:
            if line == '':
                continue
            if '|' in line:
                rules.append(line)
            else:
                updates.append(line)

    rules_dict, updates_list = parse_input(rules, updates)

    correct_middle_pages = []
    incorrect_middle_pages = []

    for update in updates_list:
        if is_update_correct(rules_dict, update):
            correct_middle_pages.append(find_middle_page(update))
        else:
            reordered_update = reorder_update(rules_dict, update)
            incorrect_middle_pages.append(find_middle_page(reordered_update))

    sum_correct = sum(correct_middle_pages)
    sum_incorrect = sum(incorrect_middle_pages)

    print("Sum of middle pages for correctly ordered updates:", sum_correct)
    print("Sum of middle pages for incorrectly ordered updates:", sum_incorrect)

if __name__ == "__main__":
    main()
