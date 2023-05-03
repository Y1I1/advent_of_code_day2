def round_score_tup(arr):
    arr = tuple(arr)    #rock              #paper           #scissors
    score_dict = {('A', 'X'):(3, 1),('A', 'Y'):(6, 2),('A', 'Z'):(0, 3),
                  ('B', 'X'):(0, 1), ('B', 'Y'):(3, 2), ('B', 'Z'):(6, 3),
                    ('C', 'X'):(6, 1), ('C', 'Y'):(0, 2), ('C', 'Z'):(3, 3), }
    return score_dict.get(arr)

def round_arr(line):
    line = line.strip('\n')
    return line.split(' ')

with open('advent_of_code/day_2_input.txt', 'r') as f:
    total = 0
    for line in f:
        total += sum(round_score_tup(round_arr(line)))

print(total)