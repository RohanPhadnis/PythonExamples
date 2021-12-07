speed = float(input('enter your speed: '))
road_type = input('enter road type (residential, main, or freeway): ')

if road_type == 'residential':
    if speed > 25:
        print('You are speeding! Drive under 25 mph!')
    else:
        print('You are within the 25 mph speed limit.')
elif road_type == 'main':
    if speed > 35:
        print('You are speeding! Drive under 35 mph!')
    else:
        print('You are within the 35 mph speed limit.')
else:
    if speed > 65:
        print('You are speeding! Drive under 65 mph!')
    else:
        print('You are within the 65 mph speed limit.')
