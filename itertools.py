import itertools

# Count function takes in a start and step arguments
# It's default starts at 1 and increments by 1
# if ran by itself, it will count forever until exiting out
def print_infinite_count():
    for num in itertools.count():
        print(num)

foods = ['apple', 'berry', 'cherry', 'durian', 'eggplant', 'fig', 'grapefruit',
        'honeydew', 'ice cream', 'jam']
# Pair it with the zip function
# The zip function pairs the arguments together 
# until the last item in either argument is reached
counted_foods = dict(zip(itertools.count(), foods))
# Useful for creating unique identifiers for data

# Cycle
cycled_foods = list(zip(itertools.cycle(['hate', 'love']), foods))

repeat_foods = list(itertools.repeat(foods[0], times=3))

# Combinations
students = ['Inna', 'Hannah', 'Athelia', 'Dominique', 'Annie', 'Ishani', 'Aileen',
            'Jennifer', 'Leizle', 'Masha', 'Brittany', 'Linh', 'Michelle', 'Anjelica', 
            'Tegan', 'Reyna', 'Arpa', 'Alejandra', 'Juliana', 'Anna', 'Laura S', 
            'Mia', 'Kelly H', 'Oxana', 'Kelly L', 'Laura M', 'Erica', 'Zephyr']

lab_partners = itertools.combinations(students,2)

def print_pairs():
    for tuple_pair in lab_partners:
        print(tuple_pair)

# Chains
chained_fruits_student = list(itertools.chain(foods, students))

# Accumulate list or range by adding it each iteration
numbers_list = [1,2,3,4,5]
accumulate_running_total = list(itertools.accumulate(range(1,6)))

# groupby

from harvest_solution import *

all_melon_types = make_melon_types()
melons = make_melons(all_melon_types)

def get_harvester(melon):
        return melon.harvester

# return a tuple pair of 
harvester_group = itertools.groupby(melons, get_harvester)  # (list, keyfunction)

# for harvester_tuple in harvester_group:
#     print(harvester_tuple)

# unpack the tuple pairs and list out the melons in each group
for key, group in harvester_group:
    print(key)
    for melon in group:
        print(melon)
    print()
