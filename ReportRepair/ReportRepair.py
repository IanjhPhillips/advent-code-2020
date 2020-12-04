def find_product ():
    with open('input_data.txt', 'r') as f:
        data = f.readlines()
        for i in data:
            for j in data:
                for k in data:
                    i = int(i)
                    j = int(j)
                    k = int(k)
                    if (i+j+k == 2020):
                        return i*j*k
        return -1

print (find_product())