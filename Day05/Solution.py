with open("input.txt") as data:
    boardingPasses = [i for i in data.read().splitlines()]


# Part 1
def part_1():
    highestID = 0

    for boardingPass in boardingPasses:
        row = int(boardingPass[:7].replace("F", "0").replace("B", "1"), 2)
        col = int(boardingPass[-3:].replace("L", "0").replace("R", "1"), 2)

        identification = (row * 8) + col

        if identification > highestID:
            highestID = identification

    print(f"{highestID} is the highest seat ID")


# Part 2
def part_2():
    seatsByRow = []
    for boardingPass in boardingPasses:
        row = int(boardingPass[:7].replace("F", "0").replace("B", "1"), 2)
        col = int(boardingPass[-3:].replace("L", "0").replace("R", "1"), 2)

        identification = (row * 8) + col
        seatsByRow.append(identification)

    seatsByRow.sort()
    for i in range(0, len(seatsByRow) - 1):
        if seatsByRow[i] + 1 != seatsByRow[i + 1]:
            print(f"{seatsByRow[i] + 1} is your seat ID")


# Run solutions
part_1()
part_2()
