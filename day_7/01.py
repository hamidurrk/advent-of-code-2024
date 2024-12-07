import json

operators = ['+', '*']

def generate_all_binary_combinations(length):
    combinations = []
    rng = (0, 2**length)
    for i in range(rng[0], rng[1]):
        binary = bin(i)[2:]
        binary = '0' * (length - len(binary)) + binary
        combinations.append(binary)
    return combinations
    
def generate_eqns(rhs: list):
    eqns = []
    length = len(rhs) - 1
    combinations = generate_all_binary_combinations(length)
    # print(combinations)
    for combination in combinations:
        rhs_copy = rhs.copy()
        eqn_str = f'{rhs_copy.pop(0)}'
        for choice in list(combination):
            if choice == '0':
                eqn_str += f" {operators[0]} {rhs_copy.pop(0)}"
            else:
                eqn_str += f" {operators[1]} {rhs_copy.pop(0)}"
        eqns.append(eqn_str)
    # print(eqns)
    return eqns

def calc_eqn(rhs:list, result = 0):
    if len(rhs) == 0:
        return result
    entry = rhs.pop(0)
    try:
        entry = int(entry)
        result = entry
    except:
        if entry == "+":
            result += int(rhs.pop(0))
        elif entry == "*":
            result *= int(rhs.pop(0))

    return calc_eqn(rhs, result)
            

def main():
    data_dict = {}
    eqn_dict = {}
    with open('day_7/01_ex.txt') as f:
        data = f.read().splitlines()
    for line in data:
        lhs = int(line.split(': ')[0])
        rhs = list(map(int, line.split(': ')[1].split(' ')))
        data_dict[lhs] = rhs

    for lhs, rhs in data_dict.items():
        eqn_dict[lhs] = generate_eqns(rhs)
    
    for lhs, eqns in eqn_dict.items():
        for eqn in eqns:
            result = calc_eqn(eqn.split())
            if result == lhs:
                data_dict[lhs] = True
                break
            else:
                data_dict[lhs] = False
    # print(data_dict)
    
    sum = 0
    for key, value in data_dict.items():
        if value:
            sum += key
    print(sum)
    
main()
