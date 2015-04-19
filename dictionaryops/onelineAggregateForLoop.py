from collections import defaultdict, Counter
import datetime

__author__ = 'swaps_000'

DATA = {u'604': [[1361836800, {u'14885549': 52, u'91478624': 127, u'25581439': 12, u'532617990': 4}],
                 [1361833200, {u'14885549': 38, u'91478624': 204, u'25581439': 14, u'40302362': 5, u'532617990': 2}]]}

# Using sum() with a generator:

total = sum(sum(inner[1].values()) for outer in DATA.values() for inner in outer)

# This is equivalent in behavior to the following for loop:

total = 0
for outer in DATA.values():
    for inner in outer:
        total += sum(inner[1].values())

my_dataset = [
    {
        'date': datetime.date(2013, 1, 1),
        'id': 99,
        'value1': 10,
        'value2': 10
    },
    {
        'date': datetime.date(2013, 1, 1),
        'id': 98,
        'value1': 10,
        'value2': 10
    },
    {
        'date': datetime.date(2013, 1, 2),
        'id': 99,
        'value1': 10,
        'value2': 10
    }
]


def solve(dataset, group_by_key, sum_value_keys):
    dict = defaultdict(Counter)
    for item in dataset:
        key = item[group_by_key]  # list of dicts, so we are doing a lookup on a dict with item[group_by_key]
        vals = {k: item[k] for k in sum_value_keys}  # iteravle of all the summable keys
        dict[key].update(vals)  #add all of them up, seems to work even if key is not present. that's an advantage
    return dict


print solve(my_dataset, 'date', ['value1', 'value2'])


# csv dictwriter
import csv


def csvWriter():
    toCSV = [{'name': 'bob', 'age': 25, 'weight': 200},
             {'name': 'jim', 'age': 31, 'weight': 180}]
    keys = toCSV[0].keys()
    with open('people.csv', 'wb') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(toCSV)
