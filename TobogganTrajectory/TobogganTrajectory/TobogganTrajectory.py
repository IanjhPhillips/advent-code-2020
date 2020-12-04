def increment (current, delta, max):
    return (current+delta)%max

def slope_check (delta_x, delta_y):
    x = 0
    y = 0
    with open ('example_data.txt', 'r') as f:
    
      trees = [line for line in f.readlines()]
      treeCount = 0

      row_length = len(trees[0])
      col_length = len(trees)

      while (y < col_length):
         if trees[y][x] == '#':
                treeCount += 1
         x = int(increment(x, delta_x, row_length-1))
         y += delta_y

      return (treeCount)

product = 1

product *= slope_check(1,1)
product *= slope_check(3,1)
product *= slope_check(5,1)
product *= slope_check(7,1)
product *= slope_check(1,2)

print (product)    