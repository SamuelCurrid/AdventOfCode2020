with open("input.txt") as data:
    expenses = [int(i) for i in data.read().splitlines()]


# Part 1
def part_1():
    for i in range(0, len(expenses)):
        for j in range(i, len(expenses)):
            if expenses[i] + expenses[j] == 2020:
                print(f"Part 1: {expenses[i] * expenses[j]}")
                return


# Part 2
def part_2():
    for i in range(0, len(expenses)):
        for j in range(i, len(expenses)):
            if expenses[i] + expenses[j] > 2020:
                continue
            for k in range(j, len(expenses)):
                if expenses[i] + expenses[j] + expenses[k] == 2020:
                    print(f"Part 2: {expenses[i] * expenses[j] * expenses[k]}")
                    return


# Run solutions
part_1()
part_2()
