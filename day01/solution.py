from typing import List


TEST_INPUT = """199
200
208
210
200
207
240
269
260
263"""


def read_data_from_str(string: str) -> List[int]:
    return list(map(int, string.split('\n')))


def calculate_number_of_increased_measurements(measurements: List[int]):
    num_increases = 0
    for i, mes in enumerate(measurements):
        if i > 0 and mes > measurements[i - 1]:
            num_increases += 1
    return num_increases


def calculate_number_of_increased_measurements_in_sw(measurements: List[int], sliding_window: int = 3):
    num_increases = 0
    for i in range(len(measurements) - sliding_window):
        if sum(measurements[i + 1:i + 1 + sliding_window]) > sum(measurements[i:i + sliding_window]):
            num_increases += 1
    return num_increases


test_data = read_data_from_str(TEST_INPUT)
assert calculate_number_of_increased_measurements(test_data) == 7
assert calculate_number_of_increased_measurements_in_sw(test_data) == 5


with open('day01/data.txt') as f:
    data = read_data_from_str(f.read())

num_larger_mes = calculate_number_of_increased_measurements(data)
print(num_larger_mes)
num_larger_mes_sw = calculate_number_of_increased_measurements_in_sw(data)
print(num_larger_mes_sw)
