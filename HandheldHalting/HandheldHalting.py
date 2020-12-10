import re
import copy
file_name = "input-data.txt"

#executes a command from command list and swaps the ith command jmp <-> nop
def execute (_code, ptr, acc, i):

    #if the second time vising a line of code
    if (_code[ptr][2]):
        print("here")
        return "bad"
    
    #get the values, make a copy of op
    op = '%s' %code[ptr][0]
    arg = _code[ptr][1]
    sign = arg[0]
    val = int(arg[1:])

    #set visited to true for this line
    code[ptr][2] = True

    #if line to be channged, change line
    if (ptr == i):
        
        if (op == "nop"):
            op = "jmp"
        elif op == "jmp":
            op = "nop"

    #display the line
    print (ptr, op, sign, val)

    #execute the command
    if (op == "nop"):
        ptr += 1
    elif (op == "acc"):
        acc += val if sign=="+" else -1*val
        ptr += 1
    else:
        ptr += val if sign=="+" else -1*val
    
    #move on to next line from ptr or exit if at the end
    if ptr == len(_code):
        return acc
    elif 0 <= ptr <= len(_code):
        return execute (_code, ptr, acc, i)

    #if somehow reach here, return bad
    return "bad"

#generates the code base from the file input, sets visited for all lines to false
def generate_code (lines):
    
    code = [line.split(' ') for line in lines]
    
    for command in code:
        command.append(False)
    return code
       
with open(file_name, 'r') as file:

    lines = file.readlines()
    code = generate_code(lines)

    code_length = len(code)

    for i in range(code_length):
        
        result = execute(code, 0 , 0, i)

        if (result != "bad"):
            print("acc", result)
            break

        code = generate_code(lines)


    
       

    