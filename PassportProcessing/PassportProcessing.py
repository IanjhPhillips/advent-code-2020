import re

def validate_passport(start, end, lines):
    byr = False
    iyr = False
    eyr = False
    hgt = False
    hcl = False
    ecl = False
    pid = False
    for i in range(start, end):

        byrval = re.search("byr:\d{4}", lines[i])
        year = int(byrval.group().split(':')[1]) if byrval else -1
        byr = True if byrval and (1920 <= year and year <= 2002) else byr

        iyrval = re.search("iyr:\d{4}", lines[i])
        year = int(iyrval.group().split(':')[1]) if iyrval else -1
        iyr = True if iyrval and (2010 <= year and year <= 2020) else iyr

        eyrval = re.search("eyr:\d{4}", lines[i])
        year = int(eyrval.group().split(':')[1]) if eyrval else -1
        eyr = True if eyrval and (2020 <= year and year <= 2030) else eyr

        hgtval = re.search("hgt:\d+((cm)|(in))", lines[i])
        if hgtval:
            heightGroup = hgtval.group().split(':')[1]
            height = int(heightGroup[slice(len(heightGroup)-2)])
            cm = re.search("cm", heightGroup)
            heightUnitCheck = (cm and 150 <= height <= 193) or (not cm and 59 <= height <= 76)
        else:
            heightUnitCheck = False
        hgt = True if hgtval and heightUnitCheck else hgt

        hclval = re.search("hcl:#[0-9a-f]{6}", lines[i])
        hcl = True if hclval else hcl

        eclval = re.search("ecl:(amb)|(blu)|(brn)|(gry)|(grn)|(hzl)|(oth)", lines[i])
        ecl = True if eclval else ecl

        pidval = re.search("pid:\d{9}", lines[i])
        pid = True if pidval else pid

    valid = byr and iyr and eyr and hgt and hcl and ecl and pid
    print(lines[start:end]) if valid else print()
    print("byr:", byr)
    print("iyr:", iyr)
    print("eyr:", eyr)
    print("hgt:", hgt)
    print("hcl:", hcl)
    print("ecl:", ecl)
    print("pid:", pid)
    return valid

filePath = 'example-data.txt'

with open(filePath, 'r') as file:
    validCount = 0
    lines = file.readlines()
    start = 0
    for i in range(len(lines)):
        if lines[i] == "\n":
            valid = validate_passport(start, i, lines)
            print(valid)
            validCount += 1 if valid else 0
            start = i+1
    print (validCount)


