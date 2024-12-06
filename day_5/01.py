def parse_input(rules, updates):
    rules_dict = {}
    for rule in rules:
        x, y = map(int, rule.split('|'))
        if y not in rules_dict:
            rules_dict[y] = []
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
        # print(rules, updates)

    rules_dict, updates_list = parse_input(rules, updates)

    middle_pages = []
    for update in updates_list:
        if is_update_correct(rules_dict, update):
            middle_pages.append(find_middle_page(update))

    result = sum(middle_pages)
    print("Sum of middle pages:", result)

if __name__ == "__main__":
    main()
