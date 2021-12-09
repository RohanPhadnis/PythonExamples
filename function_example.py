def total(highest):
    output = 0
    for i in range(highest + 1):
        output += i
    return output

max_num = int(input('maximum number: '))
print('The total is: ' + str(total(max_num)))
