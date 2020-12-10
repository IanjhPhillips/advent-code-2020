import re
file_name = 'example-data.txt'

def bag_search (bag_dict, bag_list):

    if len(bag_list) == 0:
        return 1

    bag_sum = 0

    for bag in bag_list:

        bag_count = int(re.search("\d+", bag).group()) if re.search("\d+", bag) else 0
        bag_type = re.search("(([a-zA-Z]*)\s){1,2}bag", bag).group() if re.search("(([a-zA-Z]*)\s){1,2}bag", bag).group else "crap"
        bag_sum += bag_count * int(bag_search(bag_dict, bag_dict[bag_type]))

    bag_sum += 1

    return bag_sum


with open(file_name, 'r') as file:
    count = 0
    lines = file.readlines

    bag_dict = {}

    for line in file.readlines():
        [bag, contents] = line.split("s contain")
        bags = re.finditer("\d+\s(([a-zA-Z]*)\s){1,2}bag", contents)
        bag_list = [bag.group() for bag in bags]
        bag_dict[bag] = bag_list

    print(bag_search(bag_dict, bag_dict["shiny gold bag"])-1)
    

for bag in bag_dict:
    print(bag, "contains", bag_dict[bag])
    print("")