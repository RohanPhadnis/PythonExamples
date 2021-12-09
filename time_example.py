import time

print('Typing Speed Test!')
print('Type the following text. Your time starts now!')
print('Eagle is the common name for many large birds of prey of the family Accipitridae. Eagles belong to several groups of genera, some of which are closely related. Most of the 60 species of eagle are from Eurasia and Africa.[1] Outside this area, just 14 species can be found—2 in North America, 9 in Central and South America, and 3 in Australia. Eagles are not a natural group but denote essentially any bird of prey large enough to hunt sizeable (about 50 cm long or more overall) vertebrate prey.')
start = time.time()
text = input('Start Typing: ')
end = time.time()
print('You took ' + str(end - start) + ' seconds to type the text')
