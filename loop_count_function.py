#word = 'banana'
#count = 0
#for letter in word:
#    if letter == 'a':
#        count = count + 1
#print count


word = raw_input('enter a word: ')
def counting():
    number = 0
    for letter in word:
        if letter == 'a':
            number = number + 1
    print number
counting()
