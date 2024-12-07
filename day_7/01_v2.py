import itertools

with open('day_7/01.txt', 'r') as f:
    operations = ['*', '+']
    correct_answers = 0
    for line in f:
        line = line.strip()
        answer = line.split(':')[0]
        numbers = line.split(':')[1].strip().split(' ')
        possible_operations = list(list(x) for x in itertools.product(operations, repeat=len(numbers)-1))
        for possbile_operation in possible_operations:
            result = int(numbers[0])
            for i in range(1, len(numbers)):
                if possbile_operation[i-1] == '*':
                    result *= int(numbers[i])
                else:
                    result += int(numbers[i])
                if result > int(answer):
                    break
            if result == int(answer):
                correct_answers += int(answer)
                break
    print(f'The total calibration results is {correct_answers}')