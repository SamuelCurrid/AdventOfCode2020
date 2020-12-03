with open("input.txt") as data:
    rows = [i for i in data.read().splitlines()]


# Part 1
def part_1():
    trees = 0

    for i in range(0, len(rows)):
        if rows[i][i * 3 % len(rows[i])] == "#":
            trees += 1

    print(f"There are {trees} trees")


# Part 2
def part_2():
    trees = [0, 0, 0, 0, 0]

    for i in range(0, len(rows)):

        for j in range(0, 4):
            if rows[i][i * (1 + (j * 2)) % len(rows[i])] == "#":
                trees[j] += 1

        if i % 2 == 0:
            if rows[i][int(i * 0.5) % len(rows[i])] == "#":
                trees[4] += 1

    print(f"There are {trees[0] * trees[1] * trees[2] * trees[3] * trees[4]} trees")


# Run solutions
part_1()
part_2()
