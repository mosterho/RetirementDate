###
### Random number generator for picking Sal's retirement date June 2021

### use either seed() or SystemRandom() to seed the generator
### SystemRandom() is not available on all systems
### see https://docs.python.org/3/library/random.html
from random import shuffle, seed, randrange, SystemRandom
#seed()
SystemRandom()

## datesx is a list of possible retirement dates in
##  June 2021 for Sal
##
datesx = [1,2,6,7,8,9,13,14,15,16,20,21,22,23,27,28,29,30]
print('\nPrint the retirement dates first, just to confirm before randomizing')
print('(may or may not include vacation days, etc.)')
print(datesx)

## perform iteration for...RANGE(k) number of times, print the first three
## iterations just to show the "shuffle" randomizer is working
print('\nThe following will prompt for a range for a random shuffle of the retirment dates above')
print('Basically, the number of times to shuffle a deck of cards')
wrk_minimum = -5
while(wrk_minimum < 5 or wrk_minimum > 5000000):
    wrk_minimum = int(input('Enter a minimum number of random shuffles (integers, no commas) (min=5, max=5,000,000): '))
wrk_maximum = 1
while((wrk_maximum < 1000 or wrk_maximum > 10000000) or wrk_minimum >= wrk_maximum):
    wrk_maximum = int(input('Enter a maximum number of random shuffles (integers, no commas, greater than entry above) (min=1000, max=10,000,000): '))

print('\nSelect a random number in the range entered above for the random shuffle of retirement dates')
idx = randrange(wrk_minimum, wrk_maximum)
print('Random shuffle this many times: ', idx)
print('\nPrint the first three randomized dates')
print('and then print the dates every 1 millionth shuffle')
for i in range(idx):
    shuffle(datesx)
    if i in (0,1,2):
        print(datesx)
    if i%1000000 == 0 and i > 1:
        print(i, ': ', datesx)


## print the final result :-)
print('\nAnd the final result is: ')
print(datesx)
