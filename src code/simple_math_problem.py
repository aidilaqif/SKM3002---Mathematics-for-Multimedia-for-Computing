# Function to solve problem 1
def solve_problem_1():
    p, q = 1, 8
    return f"\n5p + 12q = ", 5*p + 12*q

# Function to solve problem 2
def solve_problem_2():
    a, b, c = 2, 5, -(1/3)
    return f"\n(a/4) - 6(bc - a) = ", (a/4) - 6*(b*c - a)

# Function to solve problem 3
def solve_problem_3():
    x, y = 5, 7
    return f"\nTotal Ashley paid (RM) = 5x + 6y = ", 5*x + 6*y

# Function to solve problem 4
def solve_problem_4():
    x, y = 2, 2
    return f"\nWhen x = 2, y =2 \nTotal Sally paid (RM) = ", 8*x + 22*y

# Function to solve problem 5
def solve_problem_5():
    total_marbles = 1750 - 18
    containers_required = total_marbles // 40 + (1 if total_marbles % 40 != 0 else 0)
    return f"\nTotal Marbles = {total_marbles}.\nContainer Required = ", containers_required

# Map problem numbers to their respective functions
problems = {
    1: "Given p=1 and q=8, find the value 5p + 12q.",
    2: "Given a = 2, b = 5, and c = -(1/3), find the value of (a/4) - 6(bc-a).",
    3: "Ashley bought x slices of vanilla-flavored cake and y slices of chocolate-flavored cake. If the cost of one slice of vanilla-flavored cake and a slice of chocolate-flavored cake is RM5 and RM6, respectively, express the amount to be paid by Ashley in terms of x and y. State the result when x=5 and y=7.",
    4: "In a market, Miss Sally bought x kg of chicken at RM 8 per kg and y kg of beef at RM22 per kg. Show the result when x=2 and y=2.",
    5: "On a particular day, a machine produced 1750 marbles, 18 of which were substandard. After removing all the substandard marbles, the remaining marbles are packed into x containers, each with a capacity of 40 marbles. Calculate the minimum number of containers required to pack the remaining marbles."
}

# Function to display the list of available problems
def display_problems():
    print("\n_________________________________________________________________________________________________________________________________________________________________________________________________\n")
    print("\nAvailable problems:")
    for num, desc in problems.items():
        print(f"{num}. {desc}")
    print("\n_________________________________________________________________________________________________________________________________________________________________________________________________\n")

# Main program
while problems:
    display_problems()

    choice = input("\nEnter the number of the problem you want to solve (1-5), or enter 'q' to quit: ")

    if choice.lower() == 'q':
        print("Thank you for using this program!")
        break

    try:
        problem_num = int(choice)
        if problem_num in problems:
            if problem_num == 1:
                explanation, result  = solve_problem_1()
            elif problem_num == 2:
                explanation, result = solve_problem_2()
            elif problem_num == 3:
                explanation, result = solve_problem_3()
            elif problem_num == 4:
                explanation, result = solve_problem_4()
            elif problem_num == 5:
                explanation, result = solve_problem_5()

            print("Result:", explanation, result)
            del problems[problem_num]
        else:
            print("Question has been solved." if problem_num not in range(1, 6) else "Invalid choice. Please try again.")
    except ValueError:
        print("Invalid choice. Please enter a number (1-5) or 'q' to quit.")
