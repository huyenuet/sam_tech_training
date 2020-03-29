"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""


def count_diff_phone_numbers(num_list, distinct_num_list=None):
    if distinct_num_list is None:
        distinct_num_list = []
    for item in num_list:
        if item[0] not in distinct_num_list:
            distinct_num_list.append(item[0])
        if item[1] not in distinct_num_list:
            distinct_num_list.append(item[1])
    return distinct_num_list


def test():
    distinct_num_list = count_diff_phone_numbers(calls)
    distinct_num_list = count_diff_phone_numbers(texts, distinct_num_list)
    distinct_number_count = len(distinct_num_list)
    print(f"There are {distinct_number_count} different telephone numbers in the records.")


test()
