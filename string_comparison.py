word = raw_input('enter a word: ')
if word.lower() < 'banana':
    print 'Your word: ' + word + ', comes before banana'
elif word.lower() > 'banana':
    print 'Your word: ' + word + ', comes after banana'
else: print 'All right, bananas'
