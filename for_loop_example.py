start = int(input('enter a start number: '))
stop = int(input('enter a stop number: '))
total = 0

# Remember that the for loop will not include the stop value.
# It will only iterate up to the stop value.
# We need to specify a stop + 1 so that it includes the last number.
for i in range(start, stop + 1):
    total += i

print('The sum of all numbers from ' + str(start) + ' to ' + str(stop) + ' is ' + str(total) + '.')
