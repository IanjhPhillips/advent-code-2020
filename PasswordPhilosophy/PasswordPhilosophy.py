def verify_pass_by_count(min, max, charcode, passcode):
    count = 0;
    for x in range(len(passcode)):
        if passcode[x] == charcode:
            count += 1
    return (count >= min and count <= max)

def xor (a, b):
    return (a and not b) or (b and not a)

def verify_pass_by_position(a, b, charcode, passcode):
    return xor(passcode[a-1]==charcode, passcode[b-1] == charcode)

file = open("inputData.txt", "r")

validCount = 0

for l in file.readlines():
    line = l.split(": ")
    rule = line[0].split(" ")
    code = line[1]
    print(rule[0], rule[1])
    print(code)
    constraints = rule[0].split("-")
    if verify_pass_by_position(int(constraints[0]), int(constraints[1]), rule[1], code):
        print("valid \n")
        validCount+=1
    else:
        print("invalid \n")

print("result:", validCount)
