from typing import Callable
import re

# we ignore int numbers by task, only float numbers are detected.
# space + one or more number + dot + one or more number + space
numbers_pattern = r"\s\d+\.\d+\s"

# parses all float numbers from text and returns them as generator
def generator_numbers(text: str):
    number_groups = re.findall(numbers_pattern, text)

    for group in number_groups:
        yield float(group.strip())


#  parses all incomes from text (using func) and sums them all
def sum_profit(text: str, func: Callable):
    total_income = 0.0

    for income in func(text):
        total_income += income

    return total_income

if __name__ == "__main__":
    # we put excessive numbers within words and also int number, to ensure our pattern works as required
    text = "Загальний дохід працівника скла200.2дається з декількох частин: 1000.01 and 900 як основний дохід, доповнен122ий додатковими надходженнями 27.45 і 324.00 доларів."
    total_income = sum_profit(text, generator_numbers)
    print(f"Total income is: {total_income}")