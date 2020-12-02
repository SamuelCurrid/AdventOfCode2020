with open("input.txt") as data:
    policies = [i for i in data.read().splitlines()]


# Part 1
def part_1():
    valid = 0
    for policy in policies:
        lower_bound = int(policy[:policy.find("-")])
        upper_bound = int(policy[policy.find("-") + 1:policy.find(" ")])

        character = policy[policy.find(" ") + 1: policy.find(":")]
        password = policy[policy.rfind(" ") + 1:]

        count = 0
        for i in password:
            if i == character:
                count = count + 1

        if upper_bound >= count >= lower_bound:
            valid += 1

    print(f"There are {valid} valid passwords")


# Part 2
def part_2():
    valid = 0
    for policy in policies:
        first = int(policy[:policy.find("-")])
        second = int(policy[policy.find("-") + 1:policy.find(" ")])

        character = policy[policy.find(" ") + 1: policy.find(":")]
        password = policy[policy.rfind(" ") + 1:]

        if (password[first - 1] is character) ^ (password[second - 1] is character):
            valid += 1

    print(f"There are {valid} valid passwords")


# Run solutions
part_1()
part_2()
