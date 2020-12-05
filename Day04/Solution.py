import re

with open("input.txt") as data:
    passports = [i for i in data.read().split("\n\n")]


# Part 1
def part_1():

    valid = 0
    for passport in passports:
        passport = passport.replace("\n", " ")
        fields = passport.split(" ")

        if len(fields) < 8:
            if len(fields) == 7:
                if not any("cid" in s for s in fields):
                    valid += 1
        else:
            valid += 1

    print(f"There are {valid} valid passports")


# Part 2
def part_2():
    valid = 0
    for passport in passports:
        passport = passport.replace("\n", " ")
        fields = passport.split(" ")

        if len(fields) < 8:
            if len(fields) == 7:
                if any("cid" in s for s in fields):
                    continue
            else:
                continue

        for field in fields:
            if "byr" in field:
                year = int(field[field.find(":") + 1:])

                if year > 2002 or year < 1920:
                    break

            if "iyr" in field:
                year = int(field[field.find(":") + 1:])

                if year > 2020 or year < 2010:
                    break
            if "eyr" in field:
                year = int(field[field.find(":") + 1:])

                if year > 2030 or year < 2020:
                    break
            if "hgt" in field:
                if len(field) < 8:
                    break

                height = int(field[field.find(":") + 1:-2])
                type = field[-2:]

                if type == "in":
                    if height > 76 or height < 59:
                        break
                else:
                    if height > 193 or height < 150:
                        break
            if "hcl" in field:
                color = field[field.find(":") + 2:]

                if len(color) != 6 or not color.isalnum():
                    break
            if "ecl" in field:
                color = field[field.find(":") + 1:]

                if not any(x in color for x in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]):
                    break
            if "pid" in field:
                number = field[field.find(":") + 1:]

                if len(number) != 9:
                    break
        else:
            valid += 1
            continue

    print(f"There are {valid} valid passports")


# Run solutions
part_1()
part_2()
