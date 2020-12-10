file_name = 'input-data.txt'

def contains(container, element):
    for c in container:
        if element == c:
            return True
    return False

with open(file_name, 'r') as file:
    lines = file.readlines()
    groups = []
    group = []

    for line in lines:
        if (line != '\n'):
            group.append(line.strip())
        else:
            groups.append(group)
            group = []

    print(groups)

    score = 0

    for group in groups:
        group_answers = {}
        for person in group:
            for answer in person:
                if answer != '\n':
                    group_answers[answer] = group_answers[answer] + 1 if answer in group_answers else 1 

        for key in group_answers:
            if group_answers[key] == len(group):
                score+=1

    print(score)


