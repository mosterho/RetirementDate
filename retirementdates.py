###
### Random number generator for picking my retirement date March 2020

### use either seed() or SystemRandom() to seed the generator
### SystemRandom() is not available on all systems
### see https://docs.python.org/3/library/random.html
from random import shuffle, seed, randrange, SystemRandom
#seed()
SystemRandom()

## datesx is a list of possible retirement dates in March 2020
## assuming my shift is still Wednesday through Saturday
datesx = [4,5,6,7,11,12,13,14,18,19,20,21,25,26,27,28]
print('\nPrint the retirement dates first, just to confirm before randomizing')
print(datesx)

## perform iteration for...RANGE(k) number of times, print the first three
## iterations just to show the "shuffle" randomizer is working
print('\nCreate a random number 100000 to 500000 for a random shuffle loop')
idx = randrange(100000, 500000)
print('Random shuffle this many times: ', idx)
print('\nPrint the first three randomized dates')
for i in range(idx):
    shuffle(datesx)
    if i in (0,1,2):
        print(datesx)

## print the final result :-)
print('\nAnd the final result is: ')
print(datesx)
