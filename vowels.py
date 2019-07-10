vowels = ['a', 'e', 'i', 'o', 'u', 'y']
count = 0
word = input("Enter word/sentence: ")
many = 0
wordvowels = []
for letter in word:
    if letter in vowels:
        count += 1
        if letter not in wordvowels:
            wordvowels += letter
print(word + ' has ' + str(count) + ' Vowels')
print ('the vowels in ' + word + ' are: ')
print(wordvowels)
