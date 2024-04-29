import flet
from flet import Page, Text, IconButton, Row, icons

def calculate_values(page: Page):
    # Problem 1
    p = 1
    q = 8
    result1 = 5 * p + 12 * q
    page.add(Text(f"Result for problem 1: {result1}"))

    # Problem 2
    a = 2
    b = 5
    c = -(1 / 3)
    result2 = (a / 4) - 6 * (b * c - a)
    page.add(Text(f"Result for problem 2: {result2}"))

    # Problem 3
    x = 5
    y = 7
    cost_vanilla = 5
    cost_chocolate = 6
    total_cost = x * cost_vanilla + y * cost_chocolate
    page.add(Text(f"Result for problem 3 when x=5 and y=7: RM{total_cost}"))

    # Problem 4
    x = 2
    y = 2
    cost_chicken = 8
    cost_beef = 22
    total_cost = x * cost_chicken + y * cost_beef
    page.add(Text(f"Result for problem 4 when x=2 and y=2: RM{total_cost}"))

    # Problem 5
    total_marbles = 1750
    substandard_marbles = 18
    capacity_per_container = 40
    remaining_marbles = total_marbles - substandard_marbles
    containers_required = remaining_marbles // capacity_per_container + (
        1 if remaining_marbles % capacity_per_container != 0 else 0
    )
    page.add(Text(f"Minimum number of containers required: {containers_required}"))


flet.app(target=calculate_values, port=8550)
