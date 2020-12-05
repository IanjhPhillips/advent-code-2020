import re

#Validates a given passport designated by start and end line indices.
def validate_passport(start, end, lines):
    #one flag for each required field
    #loop over all lines in the passport
    #check each line for required fields, if they have it set True. Cannot set False after setting True within a passport (probably not scalable but whatever)
    byr_flag = False
    iyr_flag = False
    eyr_flag = False
    hgt_flag = False
    hcl_flag = False
    ecl_flag = False
    pid_flag = False

    valid = False

    #start end are line indices of passport. Example: passport starts on line 13 and ends on line 16. Scan everything between that in lines
    for i in range(start, end):

        print(lines[i], end='')

        #check for birth year
        byr_match = re.search("byr:\d{4}", lines[i])
        byr_year = int(byr_match.group().split(':')[1]) if byr_match else -1
        byr_flag = True if byr_match and (1920 <= byr_year and byr_year <= 2002) else byr_flag
        

        #check for issue year
        iyr_match = re.search("iyr:\d{4}", lines[i])
        iyr_year = int(iyr_match.group().split(':')[1]) if iyr_match else -1
        iyr_flag = True if iyr_match and (2010 <= iyr_year and iyr_year <= 2020) else iyr_flag
        

        #check for expiry year
        eyr_match = re.search("eyr:\d{4}", lines[i])
        eyr_year = int(eyr_match.group().split(':')[1]) if eyr_match else -1
        eyr_flag = True if eyr_match and (2020 <= eyr_year and eyr_year <= 2030) else eyr_flag
        

        #check for height
        hgt_match = re.search("hgt:\d+((cm)|(in))", lines[i])
        if hgt_match:
            heightGroup = hgt_match.group().split(':')[1]
            height = int(heightGroup[slice(len(heightGroup)-2)])
            cm = re.search("cm", heightGroup) #matches if cm, doesnt match in inches. I know its hacky but...
            heightUnitCheck = (cm and 150 <= height <= 193) or (not cm and 59 <= height <= 76)
        else:
            heightUnitCheck = False
        hgt_flag = True if hgt_match and heightUnitCheck else hgt_flag
        

        #check for hair color
        hcl_match = re.search("hcl:#[0-9a-f]{6}", lines[i])
        hcl_flag = True if hcl_match else hcl_flag
        

        #check for eye color
        ecl_match = re.search("ecl:(amb)|(blu)|(brn)|(gry)|(grn)|(hzl)|(oth)", lines[i])
        ecl_flag = True if ecl_match else ecl_flag
        

        #check for pass id
        pid_match = re.search("pid:\d{9}", lines[i])
        pid_flag = True if pid_match else pid_flag
        


    #beer ear air higget hydrochloric eckle pid
    valid = byr_flag and iyr_flag and eyr_flag and hgt_flag and hcl_flag and ecl_flag and pid_flag

    #printing for testing
    print()
    print("byr:", byr_flag)
    print("iyr:", iyr_flag)
    print("eyr:", eyr_flag)
    print("hgt:", hgt_flag)
    print("hcl:", hcl_flag)
    print("ecl:", ecl_flag)
    print("pid:", pid_flag)
    print()
    print(valid)
    print()

    return valid

#the file
filePath = 'input-data.txt'

#loop over all lines, each time an empty line is found, figure out the indeces corresponding to that passport and send to validate
with open(filePath, 'r') as file:

    validCount = 0

    lines = file.readlines()

    #the start of the current passport
    start = 0
    for i in range(len(lines)):
        if lines[i] == "\n":
            valid = validate_passport(start, i, lines)
            #print(valid)
            validCount += 1 if valid else 0
            start = i
            #start of passport is on the next line since current line is blank
    print (validCount)


